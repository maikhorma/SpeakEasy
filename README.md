# Speak Easy
An [Event Ghost](http://www.eventghost.org/) plug-in that uses the  [Microsoft Speech API](http://msdn.microsoft.com/en-us/library/hh362873.aspx) to turn voice commands into Event Ghost Events.

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

If that doesn't work, you can always try the setup guide here: https://code.google.com/p/simonsays/wiki/InstallationGuide
Specifically the SDK, since I think the rest of the environment is provided by EG.
## Usage

The example has a few ideas I had in terms of chaining commands. It first responds to "Roger", and then activates the next level of commands. You can say either "System" or "Start" to get into the next level of commands or "Mute" or "Save" to perform those actions.  If you said system or start, look at the available options there and try it out.

To change the keywords open the plugin's configuration. The format is just comma separated words.

# Credits
* [Simonsays](https://code.google.com/p/simonsays/) - Whoever wrote this script proved to me that it "shouldn't be that hard" so I finally dug in and gave it a try.
* [pyspeech] (https://code.google.com/p/pyspeech/) - Ended up using this as the main driver to start. Saved me a bunch of time due to how much I suck at threading in python.
* And of course the whole event ghost team and community. 

# Roadmap
* Cleanup/update/fix/document - This is my first EG plugin, and I have very little python experience. I'm sure to any experienced python dev my code is terrible. I'd like to get some feedback and make sure I'm moving forward on a solid base.
* Event tree usage - I came up with one that I thought works pretty well, but it's kind of a complicated configuration (and not perfect). I'm wondering if there are other better ways.
* [Dragonfly](https://code.google.com/p/dragonfly/) - The author of pyspeech has discontinued the project in favor of the much more robust dragonfly tool.  With it's features comes the complexity, but hopefully it'll be easy to integrate.
* Defined vs Free gramars - Free seems dificult with MS VR because it's not very good, the defined grammar is MUCH better, but also limited. I'd like to explore if there is a middle ground, like "google","search" in the grammar, that triggers the free grammar to take in whatever is said next.
* Configurations - update the config screens and add more options. Such as, speaker voice, free vs fixed grammar, hide/show windows speech toolbar.
* Speaking - I thought it'd be kind of nice to come up with some dictionary of "affirmative" and "negative" types, and then you can just specify what type you want, and it'll randomly pick (crude attempt at feeling more natural)
