


<head>
	<meta content="text/html; charset=UTF-8" http-equiv="content-type">
	<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body class="c14">
	<div>
		<!-- <p class="c30">
			<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 817.00px; height: 10.00px;">
				<img alt="" src="images/image2.png" style="width: 817.00px; height: 10.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="horizontal line">
			</span>
			<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 817.00px; height: 10.00px;">
				<img alt="" src="images/image2.png" style="width: 817.00px; height: 10.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="horizontal line">
			</span>
		</p> -->
		<p class="c5">
			<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 47.00px; height: 6.00px;">
				<img alt="" src="images/image6.png" style="width: 47.00px; height: 6.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="short line">
			</span>
		</p>
	</div>
	<p class="c43 title" id="h.vk178u7nusev">
		<span class="c21">
		Project 1</span>
		<span class="c11">
			<br>
		</span>
		<span>
		Solving 2x2 RPM using Verbal and/or Visual Representations</span>
	</p>
	<p class="c35">
		<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 47.00px; height: 6.00px;">
			<img alt="" src="images/image6.png" style="width: 47.00px; height: 6.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="short line">
		</span>
	</p>
	<p class="c5">
		<span class="c46">
		Aayush Kumar</span>
		<span class="c46">
			<br>
		</span>
		<span class="c42 c18 c45">
		27th September, 2017</span>
	</p>
	<p class="c5 c22">
		<span class="c2">
		</span>
	</p>
	<h1 class="c28" id="h.4lqp25cx7kth">
		<span>
		Introduction</span>
	</h1>
	<p class="c5">
		<span class="c2">
		Before I delve into the technical details, I would just like to say that this project proved to be a labor of love. My overall takeaway is that this test of intelligence is no trivial exercise for a computer as I thought it might have been. I also had a fairly decent misunderstanding of the Agents that solve such problems. I used to be under the assumption that there is very minimal rules and ideas pre-programmed into an agent, and that these things need to be derived intelligently from scratch. However, I have come to understand that rules are the foundation of many of our modern Knowledge Based Artificial Intelligences!</span>
	</p>
	<p class="c5 c22">
		<span class="c2">
		</span>
	</p>
	<p class="c5">
		<span class="c2">
		Without further ado, here is a technical approach to solving Raven&#39;s Progressive Matrices:</span>
	</p>
	<ol class="c34 lst-kix_ge7qo3u2btfs-0 start" start="1">
		<li class="c5 c36">
			<span class="c2">
			Reasoning Approach</span>
		</li>
		<li class="c5 c36">
			<span class="c2">
			Knowledge Representation and Solving Process</span>
		</li>
		<li class="c5 c36">
			<span class="c2">
			Design</span>
		</li>
		<li class="c5 c36">
			<span class="c2">
			Weaknesses</span>
		</li>
		<li class="c5 c36">
			<span class="c2">
			Criteria and Metrics</span>
		</li>
		<li class="c5 c36">
			<span class="c2">
			Comparing to Human Cognition</span>
		</li>
	</ol>
	<p class="c5">
		<span class="c32">
		Please Note: </span>
		<span class="c18">
		The following reflection assumes some prior knowledge of Raven&#39;s Progressive Matrices. As we have discussed the problem itself in earlier papers, I will simply jump straight into the approach that I was able to take. This approach differs from what I initially planned, but I do believe that it performs better in many aspects to my initial design</span>
	</p>
	<p class="c5 c22">
		<span class="c18 c23">
		</span>
	</p>
	<p class="c5 c22">
		<span class="c23 c18">
		</span>
	</p>
	<p class="c5 c22">
		<span class="c23 c18">
		</span>
	</p>
	<p class="c5 c22">
		<span class="c23 c18">
		</span>
	</p>
	<h1 class="c28" id="h.j10wcnfs65s">
		<span>
		Reasoning App</span>
		<span class="c16">
		roach</span>
	</h1>
	<h3 class="c8" id="h.ovawxjoi07ia">
		<span class="c38">
		What is your agent&#39;s reasoning approach - visual or verbal? Does your agent need to convert between one or the other?</span>
	</h3>
	<p class="c5 c22">
		<span class="c23 c18">
		</span>
	</p>
	<p class="c5">
		<span>
		My agent utilizes all verbal information provided but also checks for basic image transformations between corresponding figures. If such transformation(s) are found, a heavy weight is applied to the answer choice that analogously replicates those transformation(s). The rest of the intuition is derived from the textual clues within the supplied ProblemData.txt, which also contribute to the final confidence interval of each answer choice.</span>
	</p>
	<h1 class="c28" id="h.o78al2wbelr5">
		<span class="c16">
		Knowledge Representation and Solving Process</span>
	</h1>
	<h3 class="c8" id="h.lzr2si3oshbv">
		<span class="c38">
		How does your agent represent/store the images efficiently? What is your agent&rsquo;s overall problem-solving process?</span>
	</h3>
	<p class="c5">
		<span class="c23 c18">
		I grappled with this idea for a while, as I quickly realized that even once I did manage to match objects across figures, simply maintaining dictionaries of the changes made was not exactly scalable and would result in even more chaotic code. After much deliberation, I realized what my desired solving process was first- subtraction. I had begun imagining each figure as a variable of some sort that I could do basic arithmetic on, such that for a 2x2 RPM like the one below:</span>
		<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 234.00px; height: 219.00px;">
			<img alt="Basic Problem B-10.PNG" src="images/image3.png" style="width: 624.00px; height: 499.61px; margin-left: -57.00px; margin-top: -64.68px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="">
		</span>
	</p>
	<p class="c5">
		<span class="c24">
		C + (B - A) = &nbsp;#</span>
	</p>
	<p class="c5">
		<span class="c18">
		Or to simplify via reducing the number of arithmetic operations:</span>
	</p>
	<p class="c5">
		<span class="c24">
		B - A = &nbsp;# - C</span>
	</p>
	<p class="c5">
		<span class="c23 c18">
		and similarly:</span>
	</p>
	<p class="c5">
		<span class="c24">
		C - A = &nbsp;# - B</span>
	</p>
	<p class="c5">
		<span class="c2">
		I had gotten so hooked onto this idea of comparing differences in the context of arithmetic, as it also seemed to be much more accommodating of higher dimensionality RPMs such as the 3x3 problem seen here to the left:</span>
		<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 258.13px; height: 242.00px;">
			<img alt="Basic Problem E-03.PNG" src="images/image1.png" style="width: 466.88px; height: 372.31px; margin-left: 0.00px; margin-top: -13.67px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="">
		</span>
	</p>
	<p class="c5">
		<span class="c24">
		A + B = C&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A + D = G</span>
	</p>
	<p class="c5">
		<span class="c24">
		D + E = F&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B + E = H</span>
	</p>
	<p class="c5">
		<span class="c39">
		G + H = #&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C + F = #</span>
	</p>
	<p class="c5">
		<span class="c2">
		For the sake of our current project, only implementing the subtraction operator to get the difference between two figures would be sufficient for now. However, I wanted to design my Agent to be robust and easily be able to add various operators as needed. Now the million dollar question became: How do I make the variables of this ridiculous algebraic system?</span>
	</p>
	<p class="c5">
		<span>
		I needed to be able to represent each figure as a node of some sort that captured not only the characteristics of the objects within the image, but also the relationships between the objects, all while understanding which pairs of objects between the two figures were being operated on. Keeping track of these object mappings and constantly referencing them any time I wanted to do an operation of a figure was an ugly concept to me, and I believed that my knowledge representation should somehow be able to implicitly characterize which objects correspond to each other. In a sense, I had begun thinking about vector math for my figures. More specifically, as long as my objects are in the correct index of the feature vector, doing math between figures would just become a matter of implementing individual object arithmetic:</span>
	</p>
	<a id="t.332d46e33531fe725b854ef8c63f31a903101756">
	</a>
	<a id="t.0">
	</a>
	<table class="c44">
		<tbody>
			<tr class="c25">
				<td class="c19" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c24">
						Figure A feature Vector</span>
					</p>
				</td>
				<td class="c29" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c24">
						Figure A = [objA, objB, objC]</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c19" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c24">
						Figure B feature Vector</span>
					</p>
				</td>
				<td class="c19" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c24">
						Figure B = [objD, objE, objF]</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c19" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c24">
						Figure Subtraction (aka: element-wise object subtraction)</span>
					</p>
				</td>
				<td class="c19" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c24">
						B - A</span>
					</p>
				</td>
			</tr>
		</tbody>
	</table>
	<p class="c5">
		<span class="c2">
		However, this still fails to capture the relationships between objects within the same figure. For that I kept on thinking about the Semantic Network Graphs that we depicted in class, complete with nodes and edges. Several weeks later than I was hoping to have come up with a substantial knowledge representation, I realized that simply combining these two ideas of graphs and vector math would give me exactly what I needed: adjacency matrices that I could do math with.</span>
	</p>
	<p class="c5">
		<span class="c2">
		After trying out several different designs for the adjacency matrices that incorporated defined columns and rows, I had my first iteration of design for my knowledge representation of a figure:</span>
	</p>
	<p class="c5">
		<span class="c2">
		Figure A</span>
		<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 201.59px; height: 144.11px;">
			<img alt="" src="images/image8.png" style="width: 201.59px; height: 144.11px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="">
		</span>
	</p>
	<a id="t.b5a36290a5f241b601a7476be10ab916d40a19f4">
	</a>
	<a id="t.1">
	</a>
	<table class="c17">
		<tbody>
			<tr class="c25">
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0 c22">
						<span class="c6">
						</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c10">
						objA</span>
						<span class="c10 c13">
						1</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c15">
						objB</span>
						<span class="c15 c13">
						1</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c20">
						objC</span>
						<span class="c20 c13">
						1</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c10">
						objA</span>
						<span class="c10 c13">
						1</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						N/A</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						(in)</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c15">
						objB</span>
						<span class="c15 c13">
						1</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						N/A</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						(left-of)</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c20">
						objC</span>
						<span class="c13 c20">
						1</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						N/A</span>
					</p>
				</td>
			</tr>
		</tbody>
	</table>
	<p class="c5">
		<span class="c2">
		I decided to use numeric statuses for object deletion and addition in the first row/column. However, object deletion would still prove to be somewhat confusing and messy, as deleting an object would have to be reflected in the column/row header somehow, where 1 translated to a visible object, 0 translated to an invisible object, and -1 translated to the subtraction of a visible object from an invisible object (ie: loss of an object). In addition, doing arithmetic between two figures does not leverage the adjacency matrix indices as much and requires an extra column and row for simply representing each object twice. Although space was not a constraint for the scope of our sample problems, I still felt the urge to optimize this.</span>
	</p>
	<p class="c5">
		<span class="c2">
		My second iteration turned out much better, as i made use of the diagonal elements in the matrix and stored the objects themselves there without any identifying them by name and simply assigning them to the correct index initially and henceforth using an index to refer to them. This idea, whilst I am sure confusing at first, might become more clear below.</span>
	</p>
	<p class="c5 c22">
		<span class="c2">
		</span>
	</p>
	<p class="c5">
		<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 214.50px; height: 152.91px;">
			<img alt="" src="images/image7.png" style="width: 214.50px; height: 152.91px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="">
		</span>
	</p>
	<a id="t.60440fbd222b59a0c3b3255e357bca6064d4c52e">
	</a>
	<a id="t.2">
	</a>
	<table class="c17">
		<tbody>
			<tr class="c25">
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c10">
						obj</span>
						<span class="c10 c13">
						1</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						(in)</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						(left-of)</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c15">
						obj</span>
						<span class="c15 c13">
						1]</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c6">
						0</span>
					</p>
				</td>
				<td class="c7" colspan="1" rowspan="1">
					<p class="c5">
						<span class="c20">
						obj</span>
						<span class="c20 c13">
						1</span>
					</p>
				</td>
			</tr>
		</tbody>
	</table>
	<p class="c5 c22">
		<span class="c2">
		</span>
	</p>
	<p class="c5">
		<span>
		This way, arithmetic of adjacency matrices also becomes significantly easier, as we&#39;ve abstracted away the object labels and the indices represent a sort of numerical id for each object. Better yet, we cut down on the extra column and row as well, resulting in a knowledge representation that is concise yet easily usable to solve RPM&#39;s with.</span>
	</p>
	<h1 class="c28" id="h.1nky02f4epf6">
		<span>
		Design</span>
	</h1>
	<h3 class="c8" id="h.ne5doswx8d61">
		<span>
		Provide an overview of the design of your agent</span>
		<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 719.00px; height: 206.00px;">
			<img alt="Blank Diagram - Page 1.png" src="images/image5.png" style="width: 832.39px; height: 645.23px; margin-left: -14.67px; margin-top: -82.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="">
		</span>
		<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 536.70px; height: 326.50px;">
			<img alt="" src="images/image4.png" style="width: 536.70px; height: 326.50px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="">
		</span>
	<!-- </h3>
	<h1 class="c28" id="h.56f44x7edjwz">
	</h1> -->
	<!-- <h1 class="c12" id="h.43z6dez6t33">
		<span class="c16">
            Test
		</span>
	</h1>
	<h1 class="c12" id="h.vnajno2sd0ji">
		<span class="c16">
		</span>
	</h1>
	<h1 class="c12" id="h.n3mx3t4po1r4">
		<span class="c16">
		</span>
	</h1>
	<h1 class="c12" id="h.ui4wair0mkt">
		<span class="c16">
		</span>
	</h1>
	<h1 class="c12" id="h.ffgi2skkgalg">
		<span class="c16">
		</span>
	</h1>
	<h1 class="c12" id="h.rqhqvmwyz7t3">
		<span class="c16">
		</span>
	</h1>
	<h1 class="c12" id="h.p56iq18pumg2">
		<span class="c16">
		</span>
	</h1> -->
	<h1 class="c28" id="h.efoauag8drd5">
		<span class="c16">
		Weaknesses</span>
	</h1>
	<h3 class="c8" id="h.i85ws8se9wc5">
		<span class="c38">
		What mistakes does your agent makes? Could these mistakes be resolved within your agent&rsquo;s current approach, or are they fundamental problems with the way your agent approaches these problems?</span>
	</h3>
	<p class="c5">
		<span class="c18">
		One weak point of my agent is most certainly the object matching approach. Currently, I look for the most common matching objects in another figure and greedily assign them to the objects in my current figure. This type of greedy matching does decently well especially in terms of runtime complexity, but it is not as accurate as an optimal matching algorithm that would try to find the best overall matches between the figures. In addition, I currently only match objects from Figure A to Figures B and C, and then match objects in Figures 1, 2, 3, 4, 5, and 6 to that of B and C. Im the future, I would like to derive some sort of matching algorithm that isn&#39;t chaining matches together one at a time like my current Agent does. Instead, it would be ideal to pass in multiple figures and extract matches from that. This would also remedy the issue of an object from figure A disappearing in figures B and C, as considering an answer choice between 1 and 6 that contains this object would confuse my current algorithm into thinking this is a whole new object entirely, instead of matching it to that of A.</span>
	</p>
	<p class="c5 c22">
		<span class="c2">
		</span>
	</p>
	<h1 class="c9" id="h.tuokeblvw1po">
		<span class="c16">
		Criteria and Metrics</span>
	</h1>
	<h3 class="c9" id="h.2xr5eqbqj1u">
		<span class="c38">
		Please detail on your evaluation/performance criterias and your agent&#39;s results. Think about accuracy, efficiency and generality. Are there other metrics or scenarios under which you think your agent&#39;s performance would improve or suffer?</span>
	</h3>
	<p class="c5">
		<span class="c2">
		My agent seems to do fairly well dare I say with the 2x2 Raven&#39;s Progressive Matrices problems, as the representation and approach to the problem pose several strengths. For one, as I mentioned earlier, my agent is able to consistently pick up on object transformations and then apply those very same transformations to corresponding objects quite easily. In the future, if more unique transformations have to be accounted for, the structure of my Agent enables very little modification needed to accommodate new situations. In addition, I am able to ensure that each semantic network is represented in a decently sized numpy array which collectively take up storage of O(9n^2) or O(n^2), with n being the largest number of objects found in a single figure. This concise representation ensures a fairly speedy runtime of my algorithm and thus makes it quite performant. Where my agent lacks is in situations where no textual information is provided and the transformations between figures is different for each object. In such a case, I would have to take some time to implement a visual recognition system to label the objects individually and somehow characterize them to generate Semantic Nodes and Edges. In addition, the problem space and ontology become much larger when we break free of the ProblemData.txt files, so perhaps I would have to explore other better approaches. Another weakness of my algorithm is that the confidence intervals i generate using the simple Ratio Test aren&#39;t, well, very confident:</span>
	</p>
	<p class="c5">
		<span class="c2">
		Basic Problems B</span>
	</p>
	<a id="t.259812680871594ea455e2ac2119141588e5d15b">
	</a>
	<a id="t.3">
	</a>
	<table class="c17">
		<tbody>
			<tr class="c25">
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						1</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						2</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						3</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						4</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						5</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						6</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						7</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						8</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						9</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						10</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						11</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						12</span>
					</p>
				</td>
			</tr>
			<tr class="c25">
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						36.6%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						29.5%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						34.5%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						30.1%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						23.9%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						6.7%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						17.7%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						25.4%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						9.6%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						19.6%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						22.4%</span>
					</p>
				</td>
				<td class="c1" colspan="1" rowspan="1">
					<p class="c0">
						<span class="c4">
						17.3%</span>
					</p>
				</td>
			</tr>
		</tbody>
	</table>
	<p class="c5">
		<span>
		Although I could continue adjusting my weights, I sincerely believe that there is another better way to gauge confidence in my answer besides comparing the top two scores in the end. Perhaps along the way, I could give some sort of indication as whether or not I believe the answer I will derive is actually likely to be valid or not. One thing I have realized is that the success of my Agent largely depends on the initial object matching process, so that would potentially be a good candidate method to insert something like this into.</span>
	</p>
	<h1 class="c28" id="h.a7ftml3oon3v">
		<span class="c16">
		Comparing to Human Cognition</span>
	</h1>
	<h3 class="c8" id="h.dwxpb09usy14">
		<span class="c38">
		What does the design and performance of your agent tell us about human cognition? How is it similar, and how is it different? Has your agent&rsquo;s performance given you any insights into the way people solve these problems?</span>
	</h3>
	<p class="c5">
		<span>
		In designing and building my agent, I realized that the approach I took very closely modeled some aspects of human behavior. The idea of breaking down a problem into very small components is one that we are taught very frequently, and is a notion that massively helps the accuracy of the semantic networks. Without segmented objects, it would be difficult to understand many of the relations and patterns! This segways into another aspect of human cognition and learning, we tend to implicitly use what we believe to be true based off some sort of prior evidence to justify rules/patterns that can be applied to solve a host of different problems.</span>
	</p>
	<p class="c5 c22">
		<span class="c2">
		</span>
	</p>
	<div>
		<p class="c31">
			<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 817.00px; height: 43.00px;">
				<img alt="" src="images/image2.png" style="width: 817.00px; height: 43.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="footer">
			</span>
		</p>
	</div>
</body>
