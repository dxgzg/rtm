helperVersionReplace = "${helperVersion}"
helperNewVersionReplace = "${helperNewVersion}"
helperLoadReplace = "${helperLoad}"

helperTemp = f"""package conf

import (
    "encoding/json"
    "errors"
    "fmt"
    "os"
    "sync"
    "sync/atomic"
    "time"
)

type CfgDataConf struct {{
    {helperVersionReplace}
    Ver      int32
    LoadTime int64
    Revision int32
}}

func NewCfgDataConf(revision int32) *CfgDataConf {{
    c := &CfgDataConf{{
        Revision: revision,
        LoadTime: time.Now().Unix(),
    }}
    {helperNewVersionReplace}
    return c
}}

func (c *CfgDataConf) Load(path string) error {{
    {helperLoadReplace}
    return nil
}}

func LoadAll(path string) error {{
    revision, err := loadRevision(path)
    if err != nil {{
        return err
    }}
    verConf := NewCfgDataConf(revision.Revision)
    if err := verConf.Load(path); err != nil {{
        return err
    }}
    if err := onLoadFunc(verConf); err != nil {{
        return err
    }}
    verConf.Ver = addVersion()
    _CfgDataConfs.Store(verConf.Ver, verConf)
    return nil
}}

func Init() error {{
    go run()
    return nil
}}

func run() {{
    ticker := time.NewTicker(time.Minute)
    for {{
        select {{
        case <-ticker.C:
            tNow := time.Now().Unix()
            _CfgDataConfs.Range(func(key, value interface{{}}) bool {{
                ver := key.(int32)
                if ver == GetVersion() {{
                    return true
                }}
                v := value.(*CfgDataConf)
                if v.LoadTime+CfgDataConfCacheTime > tNow {{
                    _CfgDataConfs.Delete(key)
                }}
                return true
            }})
        }}
    }}
}}

type LoadFunc func(conf *CfgDataConf, reload bool) error

var loadFuncs []LoadFunc = make([]LoadFunc, 0)

func RegisterLoadFunc(f LoadFunc) {{
    loadFuncs = append(loadFuncs, f)
}}

func onLoadFunc(verConf *CfgDataConf) error {{
    ver := GetVersion()
    isReload := ver > 0
    for _, f := range loadFuncs {{
        if err := f(verConf, isReload); err != nil {{
            return err
        }}
    }}
    return nil
}}
"""

loadTemp = """if err := c.Load{}(path + "{}.xml"); err != nil {{
    return err
}}
"""