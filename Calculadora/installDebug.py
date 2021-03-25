import os

SDK = open("SDK.txt", "r")
linha = SDK.readlines()
SDKLocal = linha[1].replace("\n","").replace("\:",":")
os.system("cmd /C cd " + SDKLocal + "\\platform-tools ^&^& adb devices")
print("Gerando APK")
os.system("cmd /K gradlew installDebug")
