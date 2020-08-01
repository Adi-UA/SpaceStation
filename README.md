# ToTheMoon
This is our project for To The Moon and Hack (MLH)!

## What

We thought space could get pretty boring without anything to do, so we made a space "station". With our space station you can:
1. Play Polite Invaders (our Space Invaders spin-off),
2. Get an AI to play Polite Invaders (A trained model is included in the repository),
3. Watch the AI learn to play Polite Invaders,
4. Monitor the latest tweets about the Mars Perseverance Rover, and
5. Listen to music (it is a "station" after all...)


## Why

We wanted our hack to be an unnecessarily overengineered project that combined different technologies under a single metaphorical space umbrella.

## General Details:

* Polite Invaders - Our spin-off space invaders where both you and the villanous invaders (consisting of space creepers, death stars and space cookies) have one thing in common, politeness. The invaders are villanous, but in our game you
don't need to shoot them to drive them away. Instead, you aim and shoot polite emails at them so they apologize and leave. They will also respectfully apoligize and leave if they
bump into you on the way down. Getting the invaders to leave gets you 1 point each. You win if you reach a total of 42 points or if you survive for 99 seconds. 99 seconds
equal 15 space minutes, and the invaders legally have to leave if they can't invade you in that time. If any one of them manages to move past the bottom though, you lose. The invaders appear more frequently as you rack up points, so the game
only gets harder.... until 15 space minutes pass, of course. 

* AI - Left, Right, Stay and Shoot isn't really something you need a neural network for... but since our goal was overengineering we used an evolving neural network. Specifically,
we used the NeuroEvolution of Augmenting Topologies method of evolving neural networks in a reinforcement learning model. Multiple generations of genomes play the game and make decisons that are either
rewarded or punished depending on the outcome. Eventually, the neural network figures out how to play the game, and when it reaches a certain score threshold, the model is stored in a file. This file is
later loaded when you want the AI to play in a non-training scenario. The training runs at a much higher fps with a lot of the eye candy stripped while the testing is basically a copy of the normal game for humans with the execption of the neural network making the decisions.

* Music - Space is cool to look at, but it'd probably be cooler to listen to music while gazing into the goregeous abyss on the way to the moon. We added a simple music player with space tunes to jam out to.

* Persverance - We like to keep an eye on Perseverance and thought you might too, so we used Twitter's API to show you the latest progress tweets :) 


## What we used

* Technologies:
    * The eel library for the webapp which allows us to seamlessly use JavScript,HTML,and CSS with a Python backend
    * neat-python for the evolving neural network arhcitecture
    * pygame for the game, space AI and music visuals
    * The Twitter API for Perseverance tweets
* Resources:
    * We made our own space art inspired by Starwars, Minecraft, and Rick and Morty made using Pixilart
    * Astronaut background from UHDPaper.com
    * Daniel Zawadzki's CSS from templatemonster.com which served as the basis for our modifications
    * Space Music at www.bensound.com" from Bensound
    
    
# What's left

Not much. We added all the space functionality we were aiming for and we are particularly proud of how it looks. We wish the eel library worked better with pygame implicitly; our hacky workaround using subprocesses works but at a small cost to the user experience.




