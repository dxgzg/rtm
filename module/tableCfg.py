class TableCfg:
    def __init__(self, field_english_name, field_chinese_name, field_type, field_note):
        self.field_english_name = field_english_name
        self.field_chinese_name = field_chinese_name
        self.field_type = field_type
        self.field_note = field_note

    def __str__(self):
        return f"field_english_name:{self.field_english_name} field_chinese_name:{self.field_chinese_name} " \
               f"field_type:{self.field_type} field_note:{self.field_note}"
