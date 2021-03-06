# Script parses a list of past wordle answers that i found online

past_answers_to_parse = """
274	renew	March 20
273	allow	March 19
272	saute	March 18
271	movie	March 17
270	cater	March 16
269	tease	March 15
268	smelt	March 14
267	focus	March 13
266	today	March 12
265	watch	March 11
264	lapse	March 10
263	month	March 9
262	sweet	March 8
261	hoard	March 7
260	cloth	March 6
259	brine	March 5
258	ahead	March 4
257	mourn	March 3
256	nasty	March 2
255	rupee	March 1
254	choke	February 28
253	chant	February 27
252	spill	February 26
251	vivid	February 25
250	bloke	February 24
249	trove	February 23
248	thorn	February 22
247	other	February 21
246	tacit	February 20
245	swill	February 19
244	dodge	February 18
243	shake	February 17
242	caulk	February 16
241	aroma	February 15
240	cynic	February 14
239	robin	February 13
238	ultra	February 12
237	ulcer	February 11
236	pause	February 10
235	humor	February 9
234	frame	February 8
233	elder	February 7
232	skill	February 6
231	aloft	February 5
230	pleat	February 4
229	shard	February 3
228	moist	February 2
227	those	February 1
226	light	January 31
225	wrung	January 30
224	could	January 29
223	perky	January 28
222	mount	January 27
221	whack	January 26
220	sugar	January 25
219	knoll	January 24
218	crimp	January 23
217	wince	January 22
216	prick	January 21
215	robot	January 20
214	point	January 19
213	proxy	January 18
212	shire	January 17
211	solar	January 16
210	panic	January 15
209	tangy	January 14
208	abbey	January 13
207	favor	January 12
206	drink	January 11
205	query	January 10
204	gorge	January 9
203	crank	January 8
202	slump	January 7
201	banal	January 6
200	tiger	January 5
199	siege	January 4
198	truss	January 3
197	boost	January 2
196	rebus	January 1
195	unify	December 31
194	troll	December 30
193	tapir	December 29
192	aside	December 28
191	ferry	December 27
190	acute	December 26
189	picky	December 25
188	weary	December 24
187	gripe	December 23
186	craze	December 22
185	pluck	December 21
184	brake	December 20
183	baton	December 19
182	champ	December 18
181	peach	December 17
180	using	December 16
179	trace	December 15
178	vital	December 14
177	sonic	December 13
176	masse	December 12
175	conic	December 11
174	viral	December 10
173	rhino	December 9
172	break	December 8
171	triad	December 7
170	epoch	December 6
169	usher	December 5
168	exult	December 4
167	grime	December 3
166	cheat	December 2
165	solve	December 1
164	bring	November 30
163	prove	November 29
162	store	November 28
161	tilde	November 27
160	clock	November 26
159	wrote	November 25
158	retch	November 24
157	perch	November 23
156	rouge	November 22
155	radio	November 21
154	surer	November 20
153	finer	November 19
152	vodka	November 18
151	heron	November 17
150	chill	November 16
149	gaudy	November 15
148	pithy	November 14
147	smart	November 13
146	badly	November 12
145	rogue	November 11
144	group	November 10
143	fixer	November 9
142	groin	November 8
141	duchy	November 7
140	coast	November 6
139	blurt	November 5
138	pulpy	November 4
137	altar	November 3
136	great	November 2
135	briar	November 1
134	click	October 31
133	gouge	October 30
132	world	October 29
131	erode	October 28
130	boozy	October 27
129	dozen	October 26
128	fling	October 25
127	growl	October 24
126	abyss	October 23
125	steed	October 22
124	enema	October 21
123	jaunt	October 20
122	comet	October 19
121	tweed	October 18
120	pilot	October 17
119	dutch	October 16
118	belch	October 15
117	ought	October 14
116	dowry	October 13
115	thumb	October 12
114	hyper	October 11
113	hatch	October 10
112	alone	October 9
111	motor	October 8
110	aback	October 7
109	guild	October 6
108	kebab	October 5
107	spend	October 4
106	fjord	October 3
105	essay	October 2
104	spray	October 1
103	spicy	September 30
102	agate	September 29
101	salad	September 28
100	basic	September 27
99	moult	September 26
98	corny	September 25
97	forge	September 24
96	civic	September 23
95	islet	September 22
94	labor	September 21
93	gamma	September 20
92	lying	September 19
91	audit	September 18
90	round	September 17
89	loopy	September 16
88	lusty	September 15
87	golem	September 14
86	goner	September 13
85	greet	September 12
84	start	September 11
83	lapel	September 10
82	biome	September 9
81	parry	September 8
80	shrub	September 7
79	front	September 6
78	wooer	September 5
77	totem	September 4
76	flick	September 3
75	delta	September 2
74	bleed	September 1
73	argue	August 31
72	swirl	August 30
71	error	August 29
70	agree	August 28
69	offal	August 27
68	flume	August 26
67	crass	August 25
66	panel	August 24
65	stout	August 23
64	bribe	August 22
63	drain	August 21
62	yearn	August 20
61	print	August 19
60	seedy	August 18
59	ivory	August 17
58	belly	August 16
57	stand	August 15
56	first	August 14
55	forth	August 13
54	booby	August 12
53	flesh	August 11
52	unmet	August 10
51	linen	August 9
50	maxim	August 8
49	pound	August 7
48	mimic	August 6
47	spike	August 5
46	cluck	August 4
45	crate	August 3
44	digit	August 2
43	repay	August 1
42	sower	July 31
41	crazy	July 30
40	adobe	July 29
39	outdo	July 28
38	trawl	July 27
37	whelp	July 26
36	unfed	July 25
35	paper	July 24
34	staff	July 23
33	croak	July 22
32	helix	July 21
31	floss	July 20
30	pride	July 19
29	batty	July 18
28	react	July 17
27	marry	July 16
26	abase	July 15
25	colon	July 14
24	stool	July 13
23	crust	July 12
22	fresh	July 11
21	death	July 10
20	major	July 9
19	feign	July 8
18	abate	July 7
17	bench	July 6
16	quiet	July 5
15	grade	July 4
14	stink	July 3
13	karma	July 2
12	model	July 1
11	dwarf	June 30
10	heath	June 29
9	serve	June 28
8	naval	June 27
7	evade	June 26
6	focal	June 25
5	blush	June 24
4	awake	June 23
3	humph	June 22
2	sissy	June 21
1	rebut	June 20
0	cigar	June 19
"""

marked_for_deletion = []

past_answers_to_parse = past_answers_to_parse.split()
print(past_answers_to_parse)
for entry in past_answers_to_parse:
    if entry.isnumeric():
        marked_for_deletion.append(entry)
    if entry[0].isupper():
        marked_for_deletion.append(entry)


for entry in marked_for_deletion:
    past_answers_to_parse.remove(entry)

print(past_answers_to_parse)


with open("past_answers.txt", 'w') as file:
    for i in past_answers_to_parse:
        tup = (i, '\n')
        string = ''.join(tup)
        file.write(string)