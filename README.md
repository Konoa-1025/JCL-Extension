# Japanese C Language (JCL) - VS Code Extension

日本語でCプログラミングができるVS Code拡張機能です！

## 🚀 特徴

- ✅ **シンタックスハイライト**: JCLコードが美しく色分け表示
- ✅ **F5実行**: ワンキーでJCLファイルを実行
- ✅ **ファイルアイコン**: .jcファイルに専用アイコン
- ✅ **言語認識**: VS CodeがJCLファイルを正しく認識

## 📝 使い方

### 1. インストール
VS Code Marketplaceから「Japanese C Language」をインストール

### 2. JCLファイルを作成
```jcl
#含む <stdio.h>

整数型 主要関数() {
    表示("こんにちは、世界！\n");
    戻る 0;
}
```

### 3. 実行
- **F5キー**を押すだけで実行！

## 📚 JCLキーワード一覧

### 🔧 基本構文
| JCL | C言語 | 説明 |
|-----|-------|------|
| `主関数` | `int main` | メイン関数 |
| `もし` | `if` | 条件分岐 |
| `そうでなければ` | `else` | else文 |
| `そうでなければもし` | `else if` | else if文 |
| `間` | `while` | whileループ |
| `繰り返し` | `for` | forループ |
| `選択` | `switch` | switch文 |
| `続行` | `continue` | continue文 |
| `抜ける` | `break` | break文 |
| `戻る` | `return` | return文 |

### 📊 データ型
| JCL | C言語 | 説明 |
|-----|-------|------|
| `整数型` | `int` | 整数型 |
| `実数型` | `double` | 実数型 |
| `文字型` | `char` | 文字型 |
| `時刻型` | `time_t` | 時刻型 |

### 💻 入出力
| JCL | C言語 | 説明 |
|-----|-------|------|
| `出力` | `printf` | 画面出力 |
| `入力` | `scanf` | キーボード入力 |
| `文字入力` | `getchar` | 文字入力 |

### 📁 ファイル操作
| JCL | C言語 | 説明 |
|-----|-------|------|
| `ファイル開く` | `fopen` | ファイルを開く |
| `ファイル閉じる` | `fclose` | ファイルを閉じる |
| `ファイル出力` | `fprintf` | ファイルに出力 |
| `ファイル入力` | `fscanf` | ファイルから入力 |
| `ファイル設定` | `fseek` | ファイル位置設定 |
| `ファイルフラッシュ` | `fflush` | バッファフラッシュ |

### 🔤 文字列操作
| JCL | C言語 | 説明 |
|-----|-------|------|
| `文字列文字数` | `strlen` | 文字列の長さ |
| `文字列複製` | `strcpy` | 文字列コピー |
| `文字列結合` | `strcat` | 文字列結合 |

### 🧠 メモリ管理
| JCL | C言語 | 説明 |
|-----|-------|------|
| `メモリ確保` | `malloc` | メモリ確保 |
| `メモリ解放` | `free` | メモリ解放 |

### 🎲 乱数・時刻
| JCL | C言語 | 説明 |
|-----|-------|------|
| `乱数初期化` | `srand` | 乱数初期化 |
| `乱数生成` | `rand` | 乱数生成 |
| `現在時刻` | `time` | 現在時刻取得 |
| `時刻変換` | `ctime` | 時刻文字列変換 |
| `ローカル時刻` | `localtime` | ローカル時刻 |
| `時刻フォーマット` | `strftime` | 時刻フォーマット |

## 🔗 関連リポジトリ

このプロジェクトは、以下のリポジトリで構成されています：

- **[JCL-Extension](https://github.com/Konoa-1025/JCL-Extension)**: VS Code拡張機能（このリポジトリ）
- **[JCL-Engine](https://github.com/Konoa-1025/JCL-Engine)**: JCLトランスパイラエンジン

## 📋 要件

この拡張機能を使用するには、以下の要件を満たしている必要があります。

* **VS Code**: Visual Studio Codeがインストールされていること。
* **Python 3**: `runner.py` と `transpiler.py` の実行にPython 3が必要です。
* **GCC (または互換性のあるCコンパイラ)**: トランスパイルされたCコードをコンパイルするために、GCCなどのCコンパイラがシステムにインストールされ、パスが通っている必要があります。

## JCLコードの簡単な例

```jc
// これはJCLのコメントです
組み込む <標準入出力> // C言語のstdio.hに相当

主関数() {
    出力("こんにちは、世界！\n"); // コンソールに出力
    整数型 数値 = 10;
    もし(数値 > 5) {
        出力("数値は5より大きいです。\n");
    } そうでなければ {
        出力("数値は5以下です。\n");
    }
    戻る 0;
}
```

## How to Use (使用方法)

1. VS Codeにこの拡張機能をインストールします。
2. VS CodeでJCLファイル（.jc 拡張子のファイル）を開きます。
3. F5キーを押します。
4. 自動的にJCLコードがCにトランスパイルされ、コンパイル、実行されます。結果は新しいターミナルウィンドウに表示されます。

## 🤖 自動生成コードについて

JCLで作成されたプログラムをCにトランスパイルすると、コード中に**「JCLによって自動生成されました」**というコメントが含まれることがあります。

### なぜこの表記があるのか？

これらのコメントは、JCLトランスパイラが自動的に追加する機能コードに付けられています：

1. **文字化け防止**: 
   - `printf()` 関数の後に自動的に `fflush(stdout);` を追加
   - 日本語出力時の文字化けを防止

2. **日本語環境設定**:
   - `main()` 関数の開始時に `setlocale(LC_ALL, "ja_JP.UTF-8");` を自動挿入
   - 日本語文字の正しい表示を保証

3. **必要なヘッダファイル**:
   - `#include <locale.h>` を自動的に追加
   - ロケール設定に必要なライブラリを自動インクルード

これらの自動生成コードにより、JCLユーザーは日本語の処理について詳しく知らなくても、正しく日本語が表示されるプログラムを作成できます。

c言語のみで開発する場合は不必要です。

## Known Issues (既知の問題)

現時点では特定の既知の問題はありませんが、もし問題を発見した場合は、GitHubリポジトリのIssuesページにご報告ください。

## Release Notes (リリースノート)

### 0.0.1 (Initial Release)

- JapaneseC言語のシンタックスハイライトを追加しました。
- `.jc`, `.c`, `.out` ファイルのカスタムアイコンを追加しました。
- F5キーでのJCLコードのトランスパイル、コンパイル、実行機能を追加しました。

## License (ライセンス)

この拡張機能は、以下のMITライセンスの下で公開されています。

```
MIT License

Copyright (c) 2025 Norifumi Kondo(Studio.Δ). All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

著作権表示:  
Copyright (c) 2025 Norifumi Kondo(Studio.Δ). All rights reserved.

Enjoy!

# jc-lang Project 2025

**jc言語**は、日本語で書けるC言語ベースの教育用プログラミング言語です。  
初心者でもプログラムの構造を直感的に理解できるように設計されています。

この言語は、**U-22プログラミング・コンテスト**への応募作品として開発されています。