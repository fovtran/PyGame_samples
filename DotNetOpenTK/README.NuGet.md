## VS2019 Paths
- "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\Common7\Tools\vsdevcmd
- "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\vc\Auxiliary\Build\vcvarsall.bat" x64
- Para no participar en la telemetría si establece la variable de entorno DOTNET_CLI_TELEMETRY_OPTOUT en "1" o "true".


## NuGet Quick Guide
#### Configuration file NuGet.config Path
nuget.exe config -set repositoryPath=.\packages -configfile .\.nuget\NuGet.config

#### Restore Packages using Packages.config and NuGet.config
nuget.exe restore -configfile .\.nuget\NuGet.config
msbuild -t:restore
dotnet restore
