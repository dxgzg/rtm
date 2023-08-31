TABLE_NAME_REPLACE = "${TableName}"
TABLE_FIELDS_REPLACE = "${tableContent}"
TABLE_MANGER_REPLACE = "${tableManger}"
TABLE_MAP_REPLACE = "${tableMap}"

GO_TEMPLATE_CODE = f'''package conf

import "encoding/json"
import "errors"
import "fmt"
import "os"

type {TABLE_NAME_REPLACE} struct {{
{TABLE_FIELDS_REPLACE}
}}

type {TABLE_MANGER_REPLACE} struct {{
    {TABLE_MAP_REPLACE} map[uint32]*{TABLE_NAME_REPLACE}
}}

func New{TABLE_MANGER_REPLACE}(c *CfgDataConf) *{TABLE_MANGER_REPLACE} {{
    return &{TABLE_MANGER_REPLACE}{{
            {TABLE_MAP_REPLACE}: make(map[uint32]*{TABLE_NAME_REPLACE}, 0),
    }}
}}

func (m *{TABLE_MANGER_REPLACE}) Get{TABLE_NAME_REPLACE}(id uint32) (ptr *{TABLE_NAME_REPLACE}, ok bool) {{
    ptr, ok = m.{TABLE_MAP_REPLACE}[id]
    
    return
}}

func (m *{TABLE_MANGER_REPLACE}) Get{TABLE_MAP_REPLACE}() map[uint32]*{TABLE_NAME_REPLACE} {{
    return m.{TABLE_MAP_REPLACE}
}}

func (m *{TABLE_MANGER_REPLACE}) Get{TABLE_NAME_REPLACE}Array() []*{TABLE_NAME_REPLACE} {{
    return m.{TABLE_NAME_REPLACE}
}}

func (m *{TABLE_MANGER_REPLACE}) Load{TABLE_NAME_REPLACE}(path string) error {{
    content, err := os.ReadFile(path)
    if err != nil {{
        return errors.New(fmt.Sprintf("Load {TABLE_NAME_REPLACE} fail err=%v", err))
    }}
    
    err = json.Unmarshal(content,m)
    if err != nil {{
        return errors.New(fmt.Sprintf("Load {TABLE_NAME_REPLACE} unmarshal fail err=%v", err))
    }}
    
    for i, c := range m.{TABLE_NAME_REPLACE} {{
        m.{TABLE_MAP_REPLACE}[c.Id] = m.{TABLE_NAME_REPLACE}[i]
    }}
    return err
}}
'''
