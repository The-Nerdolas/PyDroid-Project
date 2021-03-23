import os
import shutil
import time

def main():
    #criação
    nameProject = input("Nome do projeto\n")
    packageName = input("Nome do pacote\nExemplo: com.example.br\n")
    path = input("Path\nExemplo: C:/AndroidProject/\n")
    SDK = open("SDK.txt", "r")
    linha = SDK.readlines()
    print("SDK:", linha[1].replace("\n",""))
    #Configuração do Android
    android = 0
    SDKLocal = linha[1].replace("\n","").replace("\:",":")
    for i in os.listdir(SDKLocal + "\\platforms"):
        if(int(i[-2:])>= android):
            android = int(i[-2:])
    print("Android: android-"+str(android))
    print("Path: " + path + nameProject)
    print("Criando Projeto")
    os.system("cmd /C cd "+SDKLocal+"\\tools"+"^&^& android create project --gradle  --gradle-version 3.4.2 --activity MainActivity --package " + packageName +
                  " --target "+ "android-"+str(android) +" --path " + path + nameProject)

    #Execução das outras funções
    configGradle(path,nameProject)
    execGradle(path,nameProject)
    modifArq(path,nameProject,packageName)
    


def configGradle(path,nameProject):
    #Configurações
    print("Configurando gradle")
    shutil.copy("gradleConfig/gradle/wrapper/gradle-wrapper.properties" , path + nameProject + "/gradle/wrapper/gradle-wrapper.properties")
    shutil.copy("gradleConfig/build.gradle", path + nameProject )
    shutil.copy("gradleConfig/gradlew", path + nameProject )
    shutil.copy("gradleConfig/gradlew.bat", path + nameProject )
    shutil.copy("gradleConfig/installDebug.py", path + nameProject )
    shutil.copy("SDK.txt", path + nameProject )
    #Gera local.properties (SDK PATH) 
##    localProperties = open(path + nameProject + "/local.properties", "w")
##    localProperties.write("sdk.dir=" + sdkPath)
##    localProperties.close()

def execGradle(path,nameProject):
    print("Verificando")
    #Executar comandos do gradle para verificar
    os.system("cmd /C cd " + path + nameProject + "^&^& gradlew tasks")
    os.system("cmd /C cd " + path + nameProject + "^&^& gradlew build")
    

def modifArq(path,nameProject,packageName):
    #Apagar arquivos desnecessários do projeto
    for i in os.listdir(path + nameProject + "/src/main/res/"):
        if(i != "layout"):
            shutil.rmtree(path + nameProject + "/src/main/res/" + i)
        

    #Copiar arquivos de resources
    for i in os.listdir("androidConfig/resources/"):
        shutil.copytree("androidConfig/resources/" + i, path + nameProject + "/src/main/res/" + i)

    #Copiar AndroidManifest
    shutil.copy("androidConfig/AndroidManifest.xml", path + nameProject + "/src/main/")

    #Alterar AndroidManifest
    manifest = open(path + nameProject + "/src/main/AndroidManifest.xml", "r")
    linhas = manifest.readlines()
    linhas.insert(2, '    package="'+packageName+'">')
    linhas.insert(9, 'android:label="'+nameProject+'"')
            
    manifest = open(path + nameProject + "/src/main/AndroidManifest.xml", "w")
    manifest.writelines(linhas) 
    manifest.close()

    print(":)")
    time.sleep(2)


    
    
#Exec função main()
if __name__ == '__main__':
    main()









