#define AppName "Facebook Comment Helper"
#define AppVersion "0.1"
#define AppExeName "FacebookCommentHelper"

[Setup]
AppName="Facebook Comment Helper"
AppVersion="0.1"
DefaultDirName={pf64}\FacebookCommentHelper
DefaultGroupName=FacebookCommentHelper

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Files]
Source: "C:\Users\atlanmod\Desktop\facebook-comment-util\installation\WinPython-64bit-2.7.13.1Zero\python-2.7.13.amd64\*"; DestDir: "{app}\python-2.7.13.amd64"; Flags: ignoreversion recursesubdirs createallsubdirs;
Source: "C:\Users\atlanmod\Desktop\facebook-comment-util\installation\WinPython-64bit-2.7.13.1Zero\settings\*"; DestDir: "{app}\settings"; Flags: ignoreversion recursesubdirs createallsubdirs;
Source: "C:\Users\atlanmod\Desktop\facebook-comment-util\installation\WinPython-64bit-2.7.13.1Zero\tools\*"; DestDir: "{app}\tools"; Flags: ignoreversion recursesubdirs createallsubdirs;

[Icons]
Name: "{app}\FacebookCommentHelper.exe"; Filename: "{app}\python-2.7.13.amd64\python.exe"; WorkingDir: "{app}"; Parameters: """{app}\tools\facebook-comment-util\gui\comment_helper_gui.py""";
Name: "{userdesktop}\FacebookCommentHelper"; Filename: "{app}\python-2.7.13.amd64\python.exe"; WorkingDir: "{app}"; Parameters: """{app}\tools\facebook-comment-util\gui\comment_helper_gui.py""";

