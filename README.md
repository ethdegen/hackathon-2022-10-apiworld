# Hackathon

## Generated Graphic Output

An animated GIF in Notion snazzified with the help of Picsart's APIs (e.g. changing background color and adding effects):

![totoro 2.GIF](README/totoro_2.gif)

## Running the Demo Code

Open a Visual Studio Code DevContainer then `python backend/src/domain/test.py`

## Inspiration
Popular business-savvy applications such as Notion permit embedding of graphics, but are lacking in features when it comes to snazzifying those graphics beyond basic manipulations like resizing. Headline graphics have to be interesting and eye-catching in order to inspire attention to the document and content at hand. The Picsart API can be leveraged in conjunction with APIs exposed by SaaS like Notion to automagically snazzify graphics.

## What it does
We aimed to create a backend integration that pulls content from Notion, scans it for graphics, snazzifies those graphics using Picsart's APIs such as Style Transfer, and injects the snazzified graphic back into the document by updating its embedded image URLs. By having a backend integration running silently on a server, the snazzification process works like automagic from users' perspectives.

## How we built it
We wrote a Python program, intended to be run on a server and triggered periodically by something like a cron job or webhook.

## Challenges we ran into
Not enough time!

## Accomplishments that we're proud of
We like the pieces we created and we can see how they could fit together to deliver the promised automagic snazzification of headline graphics.

## What we learned
Graphic manipulation in popular business-savvy applications such as Notion is an underserved function. People commonly paste graphics into documents, but lack effective tooling to make headline graphics and consequently their documents really stand out. Snazzy headline graphics captures both eyeballs and attention!

## What's next for Picturesque Beautifications
We would like to further refine the idea beyond a hackathon to really derive value by plugging the gap that exists today in terms of making it easy to create attention-grabbing documents that stand out through the use of snazzy graphics that are not yet easy enough to create today.

## Input Graphics

A series of still images that get enhanced via Picsart then combined into a single animated GIF for ultimate snazziness:

![697A32FB-678D-4B02-9B21-AA0995D2E960.jpeg](README/697A32FB-678D-4B02-9B21-AA0995D2E960.jpeg)

![D89137F3-A39E-48DE-9D1A-03BA4E75BF73.jpeg| width=20%](README/D89137F3-A39E-48DE-9D1A-03BA4E75BF73.jpeg)

![26E0ADA6-EB39-4017-9DBD-9879CCD16971.jpeg](README/26E0ADA6-EB39-4017-9DBD-9879CCD16971.jpeg)

![E991ADEE-8047-4684-B61A-98135FAC785C.jpeg](README/E991ADEE-8047-4684-B61A-98135FAC785C.jpeg)

![693141F3-5A27-4647-9788-A960B1C030D6.jpeg](README/693141F3-5A27-4647-9788-A960B1C030D6.jpeg)

![822BF04F-C446-4944-A530-7A34DC020354.jpeg](README/822BF04F-C446-4944-A530-7A34DC020354.jpeg)

![EBD128AC-2220-45B7-B90C-E1D1E931FC95.jpeg](README/EBD128AC-2220-45B7-B90C-E1D1E931FC95.jpeg)

![348AC19A-ABF4-4E65-96F1-504D39C903E4.jpeg](README/348AC19A-ABF4-4E65-96F1-504D39C903E4.jpeg)

![2C6C445A-2464-4E45-81A9-78328634EF60.jpeg](README/2C6C445A-2464-4E45-81A9-78328634EF60.jpeg)

![C6780E4A-4962-49BF-9978-7FB7BFA3A7D8.jpeg](README/C6780E4A-4962-49BF-9978-7FB7BFA3A7D8.jpeg)

![4EFA8CD6-D9BC-46A1-85F6-5DD9B5F590D3.jpeg](README/4EFA8CD6-D9BC-46A1-85F6-5DD9B5F590D3.jpeg)

![28CFF98B-DE84-4D0B-80D3-D098FBDBE401.jpeg](README/28CFF98B-DE84-4D0B-80D3-D098FBDBE401.jpeg)

![8A9DA382-5E56-4A49-BFA4-95CCC05CD410.jpeg](README/8A9DA382-5E56-4A49-BFA4-95CCC05CD410.jpeg)

![4960FC59-3A91-4495-BB7B-2BE546442983.jpeg](README/4960FC59-3A91-4495-BB7B-2BE546442983.jpeg)

![3A56D1B0-E464-4A0C-93BC-DFA99F5E241A.jpeg](README/3A56D1B0-E464-4A0C-93BC-DFA99F5E241A.jpeg)

![041283E4-7B30-48C0-AA7E-6C1FA632ABC8.jpeg](README/041283E4-7B30-48C0-AA7E-6C1FA632ABC8.jpeg)
