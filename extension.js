const vscode = require('vscode');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

/**
 * 拡張機能のアクティベーション
 */
function activate(context) {
    console.log('JCL拡張機能がアクティブになりました');

    // デバッグアダプターファクトリを登録
    const provider = new JCLDebugAdapterDescriptorFactory();
    context.subscriptions.push(vscode.debug.registerDebugAdapterDescriptorFactory('jcl', provider));


    let runCommand = vscode.commands.registerCommand('jcl.run', () => {
        const activeEditor = vscode.window.activeTextEditor;
        if (!activeEditor) {
            vscode.window.showErrorMessage('アクティブなエディタがありません');
            return;
        }

        const document = activeEditor.document;
        if (document.languageId !== 'jcl') {
            vscode.window.showErrorMessage('これはJCLファイルではありません');
            return;
        }

        runJCLFile(document.fileName);
    });

    context.subscriptions.push(runCommand);


    const statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 100);
    statusBarItem.text = "$(play) JCL実行";
    statusBarItem.command = 'jcl.run';
    statusBarItem.tooltip = 'JCLファイルを実行';
    

    vscode.window.onDidChangeActiveTextEditor((editor) => {
        if (editor && editor.document.languageId === 'jcl') {
            statusBarItem.show();
        } else {
            statusBarItem.hide();
        }
    });

    if (vscode.window.activeTextEditor && vscode.window.activeTextEditor.document.languageId === 'jcl') {
        statusBarItem.show();
    }

    context.subscriptions.push(statusBarItem);
}

/**
 * JCLデバッグアダプターファクトリ
 */
class JCLDebugAdapterDescriptorFactory {
    createDebugAdapterDescriptor(session) {
        // インラインでデバッグアダプターを実装
        return new vscode.DebugAdapterInlineImplementation(new JCLDebugAdapter());
    }
}

/**
 * JCLデバッグアダプター
 */
class JCLDebugAdapter {
    constructor() {
        this._sendMessage = () => {};
    }

    handleMessage(message) {
        switch (message.command) {
            case 'initialize':
                this._sendMessage({
                    type: 'response',
                    request_seq: message.seq,
                    success: true,
                    command: 'initialize',
                    body: {
                        supportsConfigurationDoneRequest: true
                    }
                });
                this._sendMessage({
                    type: 'event',
                    event: 'initialized'
                });
                break;
                
            case 'configurationDone':
                this._sendMessage({
                    type: 'response',
                    request_seq: message.seq,
                    success: true,
                    command: 'configurationDone'
                });
                break;
                
            case 'launch':
                const program = message.arguments.program;
                runJCLFile(program);
                
                this._sendMessage({
                    type: 'response',
                    request_seq: message.seq,
                    success: true,
                    command: 'launch'
                });
                
                this._sendMessage({
                    type: 'event',
                    event: 'terminated'
                });
                break;
                
            case 'disconnect':
                this._sendMessage({
                    type: 'response',
                    request_seq: message.seq,
                    success: true,
                    command: 'disconnect'
                });
                break;
        }
    }

    onDidSendMessage(callback) {
        this._sendMessage = callback;
    }

    dispose() {}
}

/**
 * JCLファイルを実行
 */
function runJCLFile(filePath) {
    // 拡張機能のディレクトリからrunner.pyを探す
    const extensionPath = __dirname;
    const runnerPath = path.join(extensionPath, 'runner.py');
    
    if (!fs.existsSync(runnerPath)) {
        vscode.window.showErrorMessage(`runner.pyが見つかりません: ${runnerPath}`);
        return;
    }

    const terminal = vscode.window.createTerminal({
        name: 'JCL実行',
        cwd: path.dirname(filePath)
    });
    
    terminal.show();
    terminal.sendText(`python "${runnerPath}" "${filePath}"`);
}

/**
 * 拡張機能の非アクティベーション
 */
function deactivate() {
    console.log('JCL拡張機能が非アクティブになりました');
}

module.exports = {
    activate,
    deactivate
};
