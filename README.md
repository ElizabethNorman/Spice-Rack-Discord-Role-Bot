# Spice-Rack-Discord-Role-Bot

Our UNBC CS community is united through one incredible discord server named The Spice Rack, run by a brilliant mad woman, me! To keep ourselves organized, 
each CS class has it's own private channel, with corresponding roles granting access to the class channel. For my last year, I made the role bot myself as 
a fun summer project. It was fun! And here it is! 

## How can I use it?

Great question! Dependencies needed are:

- dotenv
- discord

Ensure you have developer mode on discord, as you will need the following ID's:

- the channel ID where the message will be posted
- your user ID
- the ID's of each role the bot will be assigning to users

And, of course, you'll need the discord token provided to you on the discord developer portal.

Fill in the user ID, channel ID and discord token in the .env file

Fill in the role ID's and update role descriptions/emoji's in the roles.py file, unless, somehow, you're also running a CS server and by conincidence the semester
is identical to the example one I've provided.

My bot is run on my lil raspberry pi in the terminal with: python3 main.py but you do you.

When all is set, go to the channel the message will be posted to and use the command: .message This command will only work if the user using the command is
the one with the corresponding user ID we put in the .env file earlier. 

The bot will post the role message and react to the post with the emoji's you selected for the roles, then people may react accordingly and be granted roles.

Wow! What a journey!

## Questions

### What if I selected the wrong role?

You'll need to manually remove it. The unselecting a react command was a whole big ordeal I really didn't want to deal with after a weekend of making this bot
so I just didn't really deal with it as this was just a lil project for us.

### Why the Spice Rack?

I really love the Spice Girls and everyone in the chat is encouraged to have a spice name.




