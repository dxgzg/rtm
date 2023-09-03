HELPER_VERSION_REPLACE = "${helperVersion}"
HELPER_NEW_MANAGER_REPLACE = "${helperNewManager}"
HELPER_LOAD_REPLACE = "${helperLoad}"

HELPER_TEMP = f"""package conf

import (
    "time"
)

var globalCfgDataConf *CfgDataConf

type CfgDataConf struct {{
    {HELPER_VERSION_REPLACE}
    Ver      int32
    LoadTime int64
    Revision int32
}}

func NewCfgDataConf(revision int32) *CfgDataConf {{
    c := &CfgDataConf{{
        Revision: revision,
        LoadTime: time.Now().Unix(),
    }}
    {HELPER_NEW_MANAGER_REPLACE}
    return c
}}

func (c *CfgDataConf) Load(path string) error {{
    {HELPER_LOAD_REPLACE}
    return nil
}}

func LoadAll(path string) error {{
    /*revision, err := loadRevision(path)
    if err != nil {{
        return err
    }}*/
    verConf := NewCfgDataConf(0)
    if err := verConf.Load(path); err != nil {{
        return err
    }}
    globalCfgDataConf = verConf
    /*if err := onLoadFunc(verConf); err != nil {{
        return err
    }}
    verConf.Ver = addVersion()
    _CfgDataConfs.Store(verConf.Ver, verConf)
    */
    
    return nil
}}
func getGlobalCfgDataConf() *CfgDataConf {{ return globalCfgDataConf }}
// 以下为注释的代码
/*
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
}}*/
"""

loadTemp = """if err := c.Load{}(path + "{}.xml"); err != nil {{
    return err
}}
"""