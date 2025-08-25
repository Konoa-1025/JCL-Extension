import re
import sys

KEYWORDS = {
    # ファイル操作
    "ファイルフォーマット出力": "fprintf",
    "ファイルフォーマット入力": "fscanf",
    "そうでなければもし": "else if",
    "ファイルフラッシュ": "fflush",
    "ローカル時刻": "localtime",
    "時刻フォーマット": "strftime",
    "そうでなければ": "else",
    "文字列文字数": "strlen",
    "文字列複製": "strcpy",
    "文字列結合": "strcat",
    "ファイル出力": "fprintf",
    "ファイル入力": "fscanf",
    "ファイル設定": "fseek",
    "ファイル閉じる": "fclose",
    "ファイル開く": "fopen",
    "乱数初期化": "srand",
    "乱数生成": "rand",
    "時刻変換": "ctime",
    "メモリ確保": "malloc",
    "メモリ解放": "free",
    "文字入力": "getchar",
    # 制御構造
    "繰り返し": "for",
    "主関数": "int main",
    # データ型
    "時刻型": "time_t",
    "整数型": "int",
    "実数型": "double",
    "文字型": "char",
    "現在時刻": "time",
    # 制御フロー
    "続行": "continue",
    "抜ける": "break",
    "選択": "switch",
    "戻る": "return",
    # 入出力
    "出力": "printf",
    "入力": "scanf",
    # 条件分岐
    "もし": "if",
    "間": "while",
}


def transpile_jc_to_c(jc_text: str) -> str:
    c_lines = []

    for line_num, line in enumerate(jc_text.splitlines()):
        original_indent = re.match(r"^\s*", line).group(0)
        trimmed_line = line.strip()

        if not trimmed_line:
            c_lines.append(line)
            continue

        processed_line = trimmed_line


        is_preprocessor_directive = False
        

        clean_directive_line = trimmed_line.split('//', 1)[0].strip()
        if clean_directive_line.endswith(';'):
            clean_directive_line = clean_directive_line[:-1].strip()
        

        if clean_directive_line.startswith("組み込む<") and clean_directive_line.endswith(">"):
            include_content = clean_directive_line[len("組み込む<") : -1]
            

            c_header_name = {
                "標準入出力": "stdio.h",
                "メモリ管理": "stdlib.h",
                "文字列操作": "string.h",
                "時間操作": "time.h",
            }.get(include_content, include_content)
            
            processed_line = f"#include <{c_header_name}>"
            c_lines.append(original_indent + processed_line)
            is_preprocessor_directive = True
        

        elif clean_directive_line.startswith("定義 "): 
            define_content = clean_directive_line[len("定義 "):]
            processed_line = f"#define {define_content}"
            c_lines.append(original_indent + processed_line)
            is_preprocessor_directive = True
        
        if is_preprocessor_directive:
            continue


        string_literals_raw = [] 
        def replace_string_with_placeholder(match):
            string_content = match.group(1) 
            string_literals_raw.append(string_content)
            return f"__STRING_PLACEHOLDER_{len(string_literals_raw) - 1}__"

        processed_line_after_string_hiding = re.sub(r'"((?:[^"\\]|\\.)*)"', replace_string_with_placeholder, processed_line)

        processed_line_after_keyword_replace = processed_line_after_string_hiding
        for jp_keyword, c_equivalent in KEYWORDS.items():
            if jp_keyword in ["絶対l型整数", "絶対h型整数", "l型整数16進", "l型整数8進", 
                              "l型整数", "h型整数", "絶対整数", "整数16進", "整数8進", 
                              "文字列", "実数", "文字", "整数", "改行"
                             ]:
                continue
            processed_line_after_keyword_replace = processed_line_after_keyword_replace.replace(jp_keyword, c_equivalent)
        
        processed_line_after_func_cast = re.sub(r"strlen\((.*?)\)", r"(int)strlen(\1)", processed_line_after_keyword_replace)

      
        final_processed_line = processed_line_after_func_cast
        
        string_literals_processed = []
        for s_val_raw in string_literals_raw:
            s_val = s_val_raw 

            s_val = s_val.replace("改行", "\\n")   
            
            s_val = s_val.replace("絶対l型整数", "%lu")
            s_val = s_val.replace("絶対h型整数", "%hu")
            s_val = s_val.replace("l型整数16進", "%lx")
            s_val = s_val.replace("l型整数8進", "%lo")
            s_val = s_val.replace("l型整数", "%ld")
            s_val = s_val.replace("h型整数", "%hd")
            s_val = s_val.replace("絶対整数", "%u")
            s_val = s_val.replace("整数16進", "%x")
            s_val = s_val.replace("整数8進", "%o")
            s_val = s_val.replace("文字列", "%s")   
            s_val = s_val.replace("整数", "%d")

        
            if trimmed_line.startswith("出力("):
                s_val = s_val.replace("実数", "%f")     
                s_val = s_val.replace("文字", "%c")    
            elif trimmed_line.startswith("入力("): 
                s_val = s_val.replace("実数", "%lf")   
                s_val = s_val.replace("文字", " %c")
            
            string_literals_processed.append(f'"{s_val}"')

        for i in range(len(string_literals_raw) - 1, -1, -1):
            final_processed_line = final_processed_line.replace(f"__STRING_PLACEHOLDER_{i}__", string_literals_processed[i], 1)
        
        processed_line = final_processed_line

        add_semicolon = True
        control_flow_keywords_no_semicolon = ["if", "else", "for", "while", "switch", "do"]
        
        if processed_line.startswith("#"): 
            add_semicolon = False
        elif processed_line.endswith("{") or processed_line.endswith("}"): 
            add_semicolon = False
        elif processed_line.endswith("},"): 
            add_semicolon = False
        elif processed_line.endswith(";"): 
            add_semicolon = False
        elif any(processed_line.startswith(kw) for kw in control_flow_keywords_no_semicolon):
            add_semicolon = False
        
        if add_semicolon:
            processed_line += ";"
        
        if processed_line.startswith("printf("):
            c_lines.append(original_indent + processed_line)
            c_lines.append(original_indent + "fflush(stdout); //JCLによって自動生成されました")
        elif processed_line.startswith("int main("):
            c_lines.append(original_indent + processed_line)
            c_lines.append(original_indent + "    setlocale(LC_ALL, \"ja_JP.UTF-8\");//JCLによって自動生成されました")
        else:
            c_lines.append(original_indent + processed_line)

    c_code = '// This code was generated by JapaneseC Language Transpiler.\n'

    c_code += '#include <locale.h>//JCLによって自動生成されました\n'

    c_code += '\n'.join(c_lines)
    return c_code