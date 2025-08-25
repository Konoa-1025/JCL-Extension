# runner.py
import subprocess
import os
import sys

from transpiler import transpile_jc_to_c

if len(sys.argv) < 2:
    print("使い方: python runner.py <japanese_c_file_path>")
    sys.exit(1)

jc_file_path = sys.argv[1]

try:
    with open(jc_file_path, "r", encoding="utf-8") as f:
        jc_source = f.read()
except FileNotFoundError:
    print(f"❌ エラー: ファイルが見つかりません。 {jc_file_path}")
    sys.exit(1)
except Exception as e:
    print(f"❌ エラー: ファイルの読み込み中に問題が発生しました。 {e}")
    sys.exit(1)

try:
    c_output = transpile_jc_to_c(jc_source)
except Exception as e:
    print(f"❌ エラー: トランスパイル中に問題が発生しました。 {e}")
    sys.exit(1)

base_name = os.path.splitext(jc_file_path)[0]
output_c_path = base_name + ".c"
executable_name = base_name + ".out"
if sys.platform == "win32":
    executable_name = base_name + ".exe"

output_dir = os.path.dirname(output_c_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

c_folder = os.path.join(output_dir, "c_files")
exe_folder = os.path.join(output_dir, "executables")
if not os.path.exists(c_folder):
    os.makedirs(c_folder)
if not os.path.exists(exe_folder):
    os.makedirs(exe_folder)

output_c_path = os.path.join(c_folder, os.path.basename(output_c_path))
executable_name = os.path.join(exe_folder, os.path.basename(executable_name))

try:
    with open(output_c_path, "w", encoding="utf-8") as f:
        f.write(c_output)
    print(f"✅ トランスパイルに成功し {output_c_path} に出力しました。")
except Exception as e:
    print(f"❌ エラー: Cファイルの保存中に問題が発生しました。 {e}")
    sys.exit(1)

compile_command = ["gcc", "-finput-charset=UTF-8", "-fexec-charset=UTF-8", output_c_path, "-o", executable_name]
try:
    print(f"⚙️ コンパイル中: {' '.join(compile_command)}")
    compile_result = subprocess.run(compile_command, capture_output=True, text=True, check=True)
    print(f"✅ コンパイルに成功しました。")
    if compile_result.stderr:
        print(f"⚠️ コンパイル警告だよ！\n{compile_result.stderr}")
except subprocess.CalledProcessError as e:
    print(f"❌ コンパイルエラーだよ！😱\n{e.stderr}")
    sys.exit(1)

run_command = [executable_name]

print(f"🚀 実行中: {' '.join(run_command)}")

if sys.platform == "win32":
    try:
        subprocess.run(["chcp", "65001"], shell=True, capture_output=True)
        subprocess.run(run_command, text=True, check=True, capture_output=False, encoding='utf-8')
        print(f"\n--- 実行が完了しました！✨ ---")
    except subprocess.CalledProcessError as e:
        print(f"❌ 実行エラーだよ！😱\n{e.stderr.strip()}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 実行エラーだよ！😱\n{e}")
        sys.exit(1)
else:
    try:
        subprocess.run(run_command, check=True, text=True, capture_output=False, stdin=sys.stdin, encoding='utf-8')
        print(f"\n--- 実行が完了しました！✨ ---")
    except subprocess.CalledProcessError as e:
        print(f"❌ 実行エラーだよ！😱\n{e.stderr.strip()}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 実行エラーだよ！😱\n{e}")
        sys.exit(1)

sys.exit(0)