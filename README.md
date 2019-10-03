#### A template for end to end testing with Selenium and Behave

## Selenium

Is a framework for automating browser interactions. More information can be found [here](https://www.seleniumhq.org/)

## Behave

Is a framework for BDD (Behaviour-Driven Development). It is a common language syntax which can be used to define steps for end to end tests. It's documentation can be found [here](https://behave.readthedocs.io/en/latest/)

## Getting Started

In order to run this project, you will need two primary things: the Appium node package and an Android emulator. If you already have an installation of the Android SDK and have an Android Virtual Device (AVD) ready to go, this process is much simpler.

### Installing Appium

To install the Appium node package, ensure that you are using a Node version > 8 and run:

```bash
npm install -g appium
```

### Installing Android SDK

If you have the Android SDK and an Android AVD previously provisioned, skip ahead to installing an apk.

First, download and install the Java JDK from [here](https://www.oracle.com/technetwork/java/javase/downloads/index.html).

If you do not have an AVD already provisioned on your computer, you have two options for creation an AVD: Android Studios, or the command line Android SDK toolset.

[Android Studio](https://developer.android.com/studio?pkg=studio) contains all of the necessary tools for managing your Android SDK installation as well as your AVDs. It is relatively easy to use, but the application is heavy as hell.

If you aren't interested in getting Android Studio for managing AVDs, you can create AVDs from the command line by downloading the [Android SDK and command line tools](http://www.androiddocs.com/sdk/index.html#Other) installer, or use your preferred package manager and command line to install the additional tools. To install from the command line:

```bash
choco install android-sdk
```

or

```bash
brew install android-sdk
```

The default installation of the Android SDK is not fully featured. You need 4 additional tools which can be installed by running:

```bash
sdkmanager "emulator"
sdkmanager "platform-tools"
sdkmanager "build-tools;29.0.2"
sdkmanager "system-images;android-29;google_apis;x86_64"
```

The last installation is the Android system image that you are going to use to create your AVD.

For more information of the [Android SDK Command line toolset](https://developer.android.com/studio/command-line).

### Creating an AVD

To create the AVD, replace `<name>` with a name for your AVD, and run the following command:

```bash
avdmanager create avd -n <name> -k "system-images;android-29;google_apis;x86_64"
```

Or, if you have Android Studio installed, instructions for creating and managing AVDs from Android Studio can be found [here](https://developer.android.com/studio/run/managing-avds).

### Installing an APK

Whether you downloaded Android Studio or the command line tools, you should now have an AVD which you can start and run. In order to do so run:

```bash
emulator -avd <name>
```

Apparently, you should be able to drag and drop install an apk to the running Android AVD. This feature seems to work about half the time. Otherwise, with the AVD open and running in the emulator you can run:

```bash
adb install <path_to_apk>
```

In this example test suite we are using the Hello World Cordova application, built for android. The .apk can be found in context/resources/ directory of this template project.

### Running the Test Suite

Now that you have an AVD provisioned, change the `context/testsettings.json` to reflect your AVD and Android application settings. [Here](http://appium.io/docs/en/writing-running-appium/caps/) is an explanation of the different required and optional capability settings when instantiating the Appium driver.

Open a new terminal and start the Appium server by issuing the command:

```bash
appium
```

At this point, you should be able to run the test suite in another terminal:

```bash
behave
```

### Troubleshooting

#### ANDROID_SDK_ROOT Related Errors

This is sort of a non-descript, go-to error for the Android SDK, but usually it means that some executable in the Android SDK cannot be found. Add the Android SDK to your environment variables:

```bash
$env:ANDROID_SDK_ROOT = <path_to_sdk>
$env:Path += ";{$env:ANDROID_SDK_ROOT}"
```

or add

```bash
export ANDROID_SDK_ROOT=<path_to_sdk>
```

to your `.bash_profile` and dotsource your bash profile.

If this does not resolve your issue, google is your friend. Try searching for your specific issue.

#### Appium Doctor

Appium also has a node package for detecting errors in the appium installation:

To install:

```bash
node install appium-doctor -g
```

To run:

```bash
appium-doctor
```

## General Architecture

This template is built using the Page-Object-Model (POM). This is a simple architectural pattern where each webpage is modelled by an object.

`environment.py` contains [environmental controls](https://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls) for the behave framework.

There are four directories contained in this project: context, features, steps and pages:

#### context

Settings and driver instantiation. This project uses a singleton pattern to represent the driver object.

#### features

Contains `.feature` files. These are text files conforming to [gherkin syntax](https://behave.readthedocs.io/en/latest/philosophy.html#the-gherkin-language).

#### steps

Contains files with test methods which are bound to steps in the `.feature` files.

#### pages

Contains all page objects, as well as locators for finding elements on the webpages.
