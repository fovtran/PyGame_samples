MAIN_FILE = TK_Visualizer
VERSION = .
BUILD_PATH = .\build\$(VERSION)
EXECUTABLE = $(MAIN_FILE).exe
EXEC_PATH = $(BUILD_PATH)\$(EXECUTABLE)

# CSHARP_SOURCE_FILES = $(wildcard */*/*.cs */*.cs *.cs)
CSHARP_SOURCE_FILES = "TK_Visualizer.cs"

BASE_PATH_WPF = C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF
CSHARP_LIBS = $(CSHARP_LIBS) /r:$(BASE_PATH_WPF)\PresentationFramework.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:$(BASE_PATH_WPF)\PresentationCore.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:$(BASE_PATH_WPF)\WindowsBase.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:Microsoft.CSharp.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Core.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Reflection.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Data.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Data.DataSetExtensions.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Net.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Net.Http.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Xaml.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Xml.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Xml.Linq.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Drawing.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:System.Windows.Forms.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/OpenTK.glcontrol.3.1.0/lib/net20/opentk.glcontrol.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/OpenTK.GLWpfControl.4.1.0/lib/netcoreapp3.1/GLWpfControl.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/Numerics.NET.1.0.43/lib/net461/numerics.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/Newtonsoft.Json.13.0.1/lib/net45/Newtonsoft.Json.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/GeoJSON.Net.1.2.22-rc/lib/net45/GeoJSON.Net.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/System.Runtime.Numerics.4.3.0/lib/netstandard1.3/System.Runtime.Numerics.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/System.Numerics.Tensors.6.0.0-rtm.21522.10/lib/net461/System.Numerics.Tensors.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/System.Numerics.Vectors.4.5.0/lib/net46/System.Numerics.Vectors.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/ZeroMQ.4.1.0.31/lib/net40/ZeroMQ.dll
CSHARP_LIBS = $(CSHARP_LIBS) /r:./packages/OpenTK.3.3.2/lib/net20/OpenTK.dll

BASE_PATH = E:\NEWSTORE\WOW2\MyTAO\DotNetOpenTK\example4
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/OpenTK.glcontrol.3.1.0/lib/net20
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/OpenTK.GLWpfControl.4.1.0/lib/netcoreapp3.1
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/Numerics.NET.1.0.43/lib/net461
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/Newtonsoft.Json.13.0.1/lib/net45
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/GeoJSON.Net.1.2.22-rc/lib/net45
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/System.Runtime.Numerics.4.3.0/lib/netstandard1.3
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/System.Numerics.Tensors.6.0.0-rtm.21522.10/lib/net461
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/System.Numerics.Vectors.4.5.0/lib/net46
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/ZeroMQ.4.1.0.31/lib/net40
CSHARP_LIBS_PATH = $(CSHARP_LIBS_PATH) /lib:$(BASE_PATH)/packages/OpenTK.3.3.2/lib/net20

CSHARP_FLAGS = /nologo /o /debug:full /target:exe /platform:x64
CSHARP_COMPILER = C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe
RM_CMD = -del /Q /F
NUGET = C:\BIN\nuget.exe

all: $(EXECUTABLE)

$(EXECUTABLE): $(CSHARP_SOURCE_FILES)
    @ $(CSHARP_COMPILER) /out:$(EXEC_PATH) /pdb:$(BUILD_PATH)\$(MAIN_FILE).pdb $(CSHARP_FLAGS) $(CSHARP_LIBS_PATH) $(CSHARP_LIBS) $(CSHARP_SOURCE_FILES)
    @ echo compiling...

run: all
		.\scripts\run.cmd $(BUILD_PATH) $(EXECUTABLE)

clean:
    @ $(RM_CMD) $(EXECUTABLE)

cleanall:
	@ $(RM_CMD) .\build .\packages

remake:
    @ $(MAKE) clean
    @ $(MAKE)

initialize:
	del /Q /S /F .\build
	del /Q /S /F .\packages
	$(NUGET) restore
	copy .\Data $(BUILD_PATH)
	copy .\packages\OpenTK.glcontrol.3.1.0\lib\net20\opentk.glcontrol.dll $(BUILD_PATH)
	copy .\packages\OpenTK.GLWpfControl.4.1.0\lib\netcoreapp3.1\glwpfcontrol.dll $(BUILD_PATH)
	copy .\packages\OpenTK.3.3.2\lib\net20\opentk.dll $(BUILD_PATH)
	copy .\packages\Numerics.NET.1.0.43\lib\net461\numerics.dll $(BUILD_PATH)
	copy .\packages\Newtonsoft.Json.13.0.1\lib\net45\newtonsoft.json.dll $(BUILD_PATH)
	copy .\packages\GeoJSON.Net.1.2.22-rc\lib\net45\geojson.net.dll $(BUILD_PATH)
	copy .\packages\System.Runtime.Numerics.4.3.0\lib\netstandard1.3\system.runtime.numerics.dll $(BUILD_PATH)
	copy .\packages\System.Numerics.Tensors.6.0.0-rtm.21522.10\lib\net461\system.numerics.tensors.dll $(BUILD_PATH)
	copy .\packages\System.Numerics.Vectors.4.5.0\lib\net46\system.numerics.vectors.dll $(BUILD_PATH)
	copy .\packages\ZeroMQ.4.1.0.31\lib\net40\zeromq.dll $(BUILD_PATH)
