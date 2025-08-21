# Build a Multimedia Player
Build an app that is functionally similar to this example project. Try not to copy the example project, give it your own personal style.

In the prior lectures, you were introduced to working with audio and video elements. In this lab, you will build out a multimedia player that will display an audio track and video with a transcript.

For the audio element, you will need to include a source element which is used to specify the media being used.

Here is an example:

<audio controls aria-label="descriptive label goes here">
  <source src="url-to-audio-goes-here" type="audio/mpeg">
</audio>
The source element can also be used in the video element like this:

<video controls width="600" aria-label="descriptive label goes here">
  <source src="link-to-mp4-goes-here" type="video/mp4">
  <!-- Remaining code goes here -->  
</video>
Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should have an h1 element for the main title of the page.
You should have three section elements.
Inside the first section element, you should have an h2 element for the title of song playing.
Below the h2 element, you should have an audio element with controls attribute and an aria-label attribute.
Inside the audio element, you should have a source element with a src attribute pointing to an audio file and a type attribute. You are free to use this audio URL if you like: https://cdn.freecodecamp.org/curriculum/js-music-player/sailing-away.mp3
Inside the second section element, you should have an h2 element for the title of the video playing.
Below the h2 element, you should have a video element with controls, width attributes and an aria-label attribute.
Inside the video element, you should have a source element with a src attribute pointing to a video file and a type attribute. You are free to use this video URL if you like: https://cdn.freecodecamp.org/curriculum/labs/What is the map method and how does it work.mp4
Below the source element, you should have a track element with a src attribute pointing to a subtitles file and a kind attribute, a srclang attribute and a label attribute.
Inside the third section element, you should have an h2 element for the title of the section eg. "Transcript".
Below the h2 element, you should have a p element with the transcript of the video.
Run the Tests (Ctrl + Enter)
Reset this lesson
Get Help
Tests
Waiting:1. You should have an h1 element.
Waiting:2. Your h1 should have some text representing the main title of the page.
Waiting:3. You should have three section elements.
Waiting:4. The first section should contain an h2 element.
Waiting:5. Your h2 should have some text representing the title of the song playing.
Waiting:6. The first section should contain an audio element.
Waiting:7. Your audio element should have a controls attribute.
Waiting:8. Your audio element should have an aria-label attribute with text describing the audio.
Waiting:9. Your audio element should have a source element.
Waiting:10. Your source element should have a src attribute pointing to an audio file.
Waiting:11. Your source element should have a type attribute with a value specifying the type of the audio.
Waiting:12. The second section should contain an h2 element.
Waiting:13. Your h2 should have some text representing the title of the video playing.
Waiting:14. The second section should contain a video element.
Waiting:15. Your video element should have a controls attribute.
Waiting:16. Your video element should have a width attribute with a value specifying the width of the video.
Waiting:17. The video element should have a source element.
Waiting:18. The source element should have a src attribute pointing to a video file.
Waiting:19. The source element should have a type attribute with a value specifying the type of video.
Waiting:20. Your video element should have a track element.
Waiting:21. Your track element should have a src attribute pointing to a subtitles file.
Waiting:22. Your track element should have a kind attribute with text describing the kind of file.
Waiting:23. Your track element should have a srclang attribute with text describing the language of the subtitles.
Waiting:24. Your track element should have a label attribute with text describing the language of the subtitles.
Waiting:25. The third section should contain an h2 element.
Waiting:26. Your h2 should have some text representing the title of the section.
Waiting:27. The third section should contain a p element for the transcript.