tableNameReplace = "${TableName}"
tableNameLowerReplace = "${tableNameLower}"
tableFieldsReplace = "${tableContent}"
tableMangerReplace = "${tableManger}"
tableMapReplace = "${tableMap}"
tableBaseReplace = "${tableBase}"

go_template_code = f'''package conf

import "encoding/json"
import "errors"
import "fmt"
import "os"

type {tableNameReplace} struct {{
{tableFieldsReplace}
}}

type {tableMangerReplace} struct {{
    {tableMapReplace} map[uint32]*{tableNameReplace}
}}

func New{tableMangerReplace}(c *VersionConf) *{tableMangerReplace} {{
    return &{tableMangerReplace}{{
            {tableMapReplace}: make(map[uint32]*{tableNameReplace}, 0),
    }}
}}

func (m *{tableMangerReplace}) Get{tableNameReplace}(id uint32) (ptr *{tableNameReplace}, ok bool) {{
    ptr, ok = m.{tableMapReplace}[id]
    {tableBaseReplace}
    
    return
}}

func (m *{tableMangerReplace}) Get{tableMapReplace}() map[uint32]*{tableNameReplace} {{
    return m.{tableMapReplace}
}}

func (m *{tableMangerReplace}) Get{tableNameReplace}Array() []*{tableNameReplace} {{
    return m.{tableNameReplace}
}}

func (m *{tableMangerReplace}) Load{tableNameReplace}(path string) error {{
    content, err := os.ReadFile(path)
    if err != nil {{
        return errors.New(fmt.Sprintf("Load {tableNameReplace} fail err=%v", err))
    }}
    
    err = json.Unmarshal(content,m)
    if err != nil {{
        return errors.New(fmt.Sprintf("Load {tableNameReplace} unmarshal fail err=%v", err))
    }}
    
    for i, c := range m.{tableNameReplace} {{
        m.{tableMapReplace}[c.Id] = m.{tableNameReplace}[i]
    }}
    return err
}}
'''
