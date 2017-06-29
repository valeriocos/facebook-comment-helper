[Setup]
AppName="Facebook Comment Helper"
AppVersion="0.1"
AppPublisher="Valerio Cosentino"
AppPublisherURL="https://valeriocos.github.io/"
AppSupportURL=https://github.com/valeriocos/facebook-comment-helper
DefaultDirName={pf64}\FacebookCommentHelper
DefaultGroupName=FacebookCommentHelper

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Files]
Source: "C:\Users\atlanmod\Desktop\facebook-comment-helper\installer\WinPython-64bit-2.7.13.1Zero\python-2.7.13.amd64\*"; DestDir: "{app}\python-2.7.13.amd64"; Flags: ignoreversion recursesubdirs createallsubdirs;
Source: "C:\Users\atlanmod\Desktop\facebook-comment-helper\installer\WinPython-64bit-2.7.13.1Zero\settings\*"; DestDir: "{app}\settings"; Flags: ignoreversion recursesubdirs createallsubdirs;
Source: "C:\Users\atlanmod\Desktop\facebook-comment-helper\installer\WinPython-64bit-2.7.13.1Zero\tools\*"; DestDir: "{app}\tools"; Flags: ignoreversion recursesubdirs createallsubdirs;

[Icons]
Name: "{app}\FacebookCommentHelper.exe"; Filename: "{app}\python-2.7.13.amd64\python.exe"; WorkingDir: "{app}"; Parameters: """{app}\tools\facebook-comment-helper\gui\comment_helper_gui.py""";
Name: "{userdesktop}\FacebookCommentHelper"; Filename: "{app}\python-2.7.13.amd64\python.exe"; WorkingDir: "{app}"; Parameters: """{app}\tools\facebook-comment-helper\gui\comment_helper_gui.py""";

