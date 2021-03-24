# Instalação de Dependencies (build.gradle)

Ao contrário do Android Studio que gera 2 arquivos build.gradle, o PyDroid gera apenas 1, mas com as mesmas funcionalidades dos 2.

Toda configuração que era feita no app/build.gradle agora é feita no build.gradle:

``` gradle
buildscript {
    
    repositories {
        google()
        jcenter()
        
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.6.3'
    }
}

allprojects {
    repositories {
        google()
        jcenter()
        
    }
}

//build.gradle-APP

apply plugin: 'com.android.application'

android {
    compileSdkVersion 28
    defaultConfig {
        applicationId "com.teste.br"
        minSdkVersion 17
        targetSdkVersion 28
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "android.support.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        debug {
            ext.enableCrashlytics = false
            ext.alwaysUpdateBuildId = false
        }
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'com.android.support:appcompat-v7:28.0.0'
    implementation 'com.android.support:design:28.0.0'
    implementation 'com.android.support.constraint:constraint-layout:1.1.3'
    implementation 'com.android.support:support-v4:28.0.0'
    implementation 'android.arch.lifecycle:extensions:1.1.1'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'com.android.support.test:runner:1.0.2'
    androidTestImplementation 'com.android.support.test.espresso:espresso-core:3.0.2'
}
```
