# COPY THIS FILE INTO A FILE CALLED config.py AND CHANGE THE VALUES AS NEEDED.
# discord API bot token https://discord.com/developers/applications
bot_token = "EXAMPLE_TOKEN"
# tenor API key https://tenor.com/developer/keyregistration
tenor_key = "EXAMPLE_KEY"
# windows executable for chromedriver https://chromedriver.chromium.org/
chrome_driver_windows = "chromedriver87.exe"
# linux binary for chromedriver https://chromedriver.chromium.org/
chrome_driver_linux = "chromedriver87"
# the number of instances of chromedriver to run for caption processing.
# more means faster processing of videos and better under heavy load but also uses more PC resources!
chrome_driver_instances = 20
# NOTICE is recommended, INFO prints more information about what bot is doing, WARNING only prints errors.
log_level = "NOTICE"
# maximum number of frames for an input file.
max_frames = 1024
# amount of seconds cooldown per user commands have. set to 0 to disable cooldown
cooldown = 1
# the text to use for different messages, can be custom emojis or just unicode
emojis = {
    "x": "<:xmark:803792052932444180>",
    "warning": "<:wmark:803791399782580284>",
    "question": "<:qmark:803791399615070249>",
    "exclamation_question": "<:eqmark:803791399501168641>",
    "2exclamation": "<:eemark:803791399710883871>",
    "working": "<a:working:803801825605320754>",
    "clock": "<:clockmark:803803703169515541>"
}
# up to 25 tips that can show when using $help tips
tips = {
    "Media Searching": "MediaForge automatically searches for any media in a channel. Reply to a message with the command to search that message first.",
    "GIFs and MP4s": "MediaForge works faster with MP4 files, due to GIF conversion not being fast.",
    "Tenor GIFs": "All tenor GIFs are interpreted as MP4s by default due to their superior quality. Use `tenorgif` to send the raw GIF url or `togif` to convert any video to a gif.",
    "Self-Hosting": "MediaForge is completely open source and anyone can host a clone themself!\nhttps://github.com/HexCodeFFF/captionbot"
}
# prefix for commands
command_prefix = "$"
