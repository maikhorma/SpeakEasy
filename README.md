# Speak Easy
An [Event Ghost](http://www.eventghost.org/) plug-in that uses the [http://msdn.microsoft.com/en-us/library/hh362873.aspx](Microsoft Speech API) (SAPI) to turn voice commands into Event Ghost Events.

## Before you begin
If your microphone is not ready for windows to use, the plugin will fail to initialize.
1. Plugin/setup/install your microphone.
2. Open the windows 7 or 8 search and type "Speech Recognition" to find the tool for setting up the microphone and start training.
3. Launch "Windows Speech Recognition".
4. Go AT LEAST as far as where it says "The microphone is ready to use with this computer." You should complete the training for best results, but so far for me just verifying that the mic is setup at least "works".

## Installation instructions

1. Install Event Ghost if you haven't already.
2. Install the MS Speech Platform SDK for your appropriate OS - http://www.microsoft.com/en-us/download/details.aspx?id=27226 
3. Download the plugin by using git's "Download as Zip" feature.
4. Extract zip to your \<Event Ghost Install Dir>\plugins folder. 
5. Rename it to just "SpeakEasy", not "SpeakEasy-master". (only matters for the example tree that's included)
5. Launch Event Ghost.
6. Click File -> Open
7. Browse to <event ghost install dir>\plugins\SpeakEasy
8. Select "SpeakEasyExample.xml" and click Open.

## Usage

The example has a few ideas I had in terms of chaining commands. It first responds to "Roger", and then activates the next level of commands. You can say either "System" or "Start" to get into the next level of commands or "Mute" or "Save" to perform those actions.  If you said system or start, look at the available options there and try it out.

To change the keywords open the plugin's configuration. The format is just comma separated words.