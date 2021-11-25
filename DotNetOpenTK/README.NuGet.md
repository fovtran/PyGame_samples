## VS2019 Paths
- "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\Common7\Tools\vsdevcmd
- "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\vc\Auxiliary\Build\vcvarsall.bat" x64
- Para no participar en la telemetría si establece la variable de entorno set DOTNET_CLI_TELEMETRY_OPTOUT=1


## NuGet Quick Guide
#### Configuration file NuGet.config Path
nuget.exe config -set repositoryPath=.\packages -configfile .\.nuget\NuGet.config

#### Restore Packages using Packages.config and NuGet.config
nuget.exe restore -configfile .\.nuget\NuGet.config
msbuild -t:restore
dotnet restore


##################
Another option is to put NuGet.config next to the solution file:

<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="nuget.org" value="https://www.nuget.org/api/v2/" />
    <add key="MyShare" value="\MyShare" />
    <add key="MyServer" value="http://MyServer" />
  </packageSources>
  <activePackageSource>
    <add key="All" value="(Aggregate source)"  />
  </activePackageSource>
</configuration>
#################
Next was to add a .nuspec file to the root directory of the solution project to build the NuGet for.

<?xml version="1.0"?>
<package xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <metadata xmlns="http://schemas.microsoft.com/packaging/2010/07/nuspec.xsd">
    <id>Foo.Bar.Package</id>
    <version>1.0.23</version>
    <authors>FooBar Industries</authors>
    <requireLicenseAcceptance>false</requireLicenseAcceptance>
    <description>FooBar Industries package</description>
  </metadata>
  <files>
    <file src="binRelease*.dll" target="libnet462" />
    <file src="binRelease-Net46*.dll" target="libnet46" />
    <file src="binRelease-Net45*.dll" target="libnet45" />
    <file src="binRelease-Net4*.dll" target="libnet40" />
  </files>
</package>
