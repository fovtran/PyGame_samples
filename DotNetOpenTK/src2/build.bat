# Build advanced http server

rem csc /r:System.Net.dll /t:library SimpleWebServer.cs
rem csc /r:System.Net.dll /r:NVelocity.dll /t:library VelocityTemplateRenderer.cs
rem csc /r:System.Net.dll,VelocityTemplateRenderer.dll,SimpleWebServer.dll Server.cs
