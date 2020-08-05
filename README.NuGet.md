# NuGet Quick Guide


#### Configuration file NuGet.config Path
nuget.exe config -set repositoryPath=.\packages -configfile .\.nuget\NuGet.config

#### Restore Packages using Packages.config and NuGet.config
nuget.exe restore -configfile .\.nuget\NuGet.config
