### A Pluto.jl notebook ###
# v0.17.2

using Markdown
using InteractiveUtils

# ╔═╡ 695cdeaa-56a8-11ec-2ea0-67a71259749e
html"<article class=\"day-desc\"><h2>--- Day 3: Binary Diagnostic ---</h2><p>The submarine has been making some <span title=\"Turns out oceans are heavy.\">odd creaking noises</span>, so you ask it to produce a diagnostic report just in case.</p>
<p>The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the <em>power consumption</em>.</p>
<p>You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the <em>gamma rate</em> and the <em>epsilon rate</em>). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.</p>
<p>Each bit in the gamma rate can be determined by finding the <em>most common bit in the corresponding position</em> of all numbers in the diagnostic report. For example, given the following diagnostic report:</p>
<pre><code>00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
</code></pre>
<p>Considering only the first bit of each number, there are five <code>0</code> bits and seven <code>1</code> bits. Since the most common bit is <code>1</code>, the first bit of the gamma rate is <code>1</code>.</p>
<p>The most common second bit of the numbers in the diagnostic report is <code>0</code>, so the second bit of the gamma rate is <code>0</code>.</p>
<p>The most common value of the third, fourth, and fifth bits are <code>1</code>, <code>1</code>, and <code>0</code>, respectively, and so the final three bits of the gamma rate are <code>110</code>.</p>
<p>So, the gamma rate is the binary number <code>10110</code>, or <code><em>22</em></code> in decimal.</p>
<p>The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is <code>01001</code>, or <code><em>9</em></code> in decimal. Multiplying the gamma rate (<code>22</code>) by the epsilon rate (<code>9</code>) produces the power consumption, <code><em>198</em></code>.</p>
<p>Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. <em>What is the power consumption of the submarine?</em> (Be sure to represent your answer in decimal, not binary.)</p>
</article>"

# ╔═╡ 1457d0de-e91b-44d1-a116-d74abe387c89
begin
	input_lines = readlines("input.txt");
	reading_size = length(input_lines[1]);
	readings = [parse(Int64, reading_str, base=2) for reading_str in input_lines];
end;

# ╔═╡ 9fcf7c54-1c01-482d-9947-7b6f7ac99570
begin
	masks = [1 << i for i in 0:(reading_size - 1)];
	counts = [0 for _ in 1:reading_size];
	for reading in readings
	     counts += ((((reading .& masks) .> 0) .<< 1) .- 1)
	end;
	gamma_bits = counts .>= 0;
	epsilon_bits = .~gamma_bits;
	gamma = sum(gamma_bits .* masks);
	epsilon = sum(epsilon_bits .* masks);
	(gamma, epsilon, gamma * epsilon)
end

# ╔═╡ 290f93c4-27ff-4857-8a47-00f2cb0f65c7
html"<article class=\"day-desc\"><h2 id=\"part2\">--- Part Two ---</h2><p>Next, you should verify the <em>life support rating</em>, which can be determined by multiplying the <em>oxygen generator rating</em> by the <em>CO2 scrubber rating</em>.</p>
<p>Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and <em>consider just the first bit</em> of those numbers. Then:</p>
<ul>
<li>Keep only numbers selected by the <em>bit criteria</em> for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.</li>
<li>If you only have one number left, stop; this is the rating value for which you are searching.</li>
<li>Otherwise, repeat the process, considering the next bit to the right.</li>
</ul>
<p>The <em>bit criteria</em> depends on which type of rating value you want to find:</p>
<ul>
<li>To find <em>oxygen generator rating</em>, determine the <em>most common</em> value (<code>0</code> or <code>1</code>) in the current bit position, and keep only numbers with that bit in that position. If <code>0</code> and <code>1</code> are equally common, keep values with a <code><em>1</em></code> in the position being considered.</li>
<li>To find <em>CO2 scrubber rating</em>, determine the <em>least common</em> value (<code>0</code> or <code>1</code>) in the current bit position, and keep only numbers with that bit in that position. If <code>0</code> and <code>1</code> are equally common, keep values with a <code><em>0</em></code> in the position being considered.</li>
</ul>
<p>For example, to determine the <em>oxygen generator rating</em> value using the same example diagnostic report from above:</p>
<ul>
<li>Start with all 12 numbers and consider only the first bit of each number. There are more <code>1</code> bits (7) than <code>0</code> bits (5), so keep only the 7 numbers with a <code>1</code> in the first position: <code>11110</code>, <code>10110</code>, <code>10111</code>, <code>10101</code>, <code>11100</code>, <code>10000</code>, and <code>11001</code>.</li>
<li>Then, consider the second bit of the 7 remaining numbers: there are more <code>0</code> bits (4) than <code>1</code> bits (3), so keep only the 4 numbers with a <code>0</code> in the second position: <code>10110</code>, <code>10111</code>, <code>10101</code>, and <code>10000</code>.</li>
<li>In the third position, three of the four numbers have a <code>1</code>, so keep those three: <code>10110</code>, <code>10111</code>, and <code>10101</code>.</li>
<li>In the fourth position, two of the three numbers have a <code>1</code>, so keep those two: <code>10110</code> and <code>10111</code>.</li>
<li>In the fifth position, there are an equal number of <code>0</code> bits and <code>1</code> bits (one each). So, to find the <em>oxygen generator rating</em>, keep the number with a <code>1</code> in that position: <code>10111</code>.</li>
<li>As there is only one number left, stop; the <em>oxygen generator rating</em> is <code>10111</code>, or <code><em>23</em></code> in decimal.</li>
</ul>
<p>Then, to determine the <em>CO2 scrubber rating</em> value from the same example above:</p>
<ul>
<li>Start again with all 12 numbers and consider only the first bit of each number. There are fewer <code>0</code> bits (5) than <code>1</code> bits (7), so keep only the 5 numbers with a <code>0</code> in the first position: <code>00100</code>, <code>01111</code>, <code>00111</code>, <code>00010</code>, and <code>01010</code>.</li>
<li>Then, consider the second bit of the 5 remaining numbers: there are fewer <code>1</code> bits (2) than <code>0</code> bits (3), so keep only the 2 numbers with a <code>1</code> in the second position: <code>01111</code> and <code>01010</code>.</li>
<li>In the third position, there are an equal number of <code>0</code> bits and <code>1</code> bits (one each). So, to find the <em>CO2 scrubber rating</em>, keep the number with a <code>0</code> in that position: <code>01010</code>.</li>
<li>As there is only one number left, stop; the <em>CO2 scrubber rating</em> is <code>01010</code>, or <code><em>10</em></code> in decimal.</li>
</ul>
<p>Finally, to find the life support rating, multiply the oxygen generator rating (<code>23</code>) by the CO2 scrubber rating (<code>10</code>) to get <code><em>230</em></code>.</p>
<p>Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. <em>What is the life support rating of the submarine?</em> (Be sure to represent your answer in decimal, not binary.)</p>
</article>"

# ╔═╡ 3c8b3203-77cd-4699-8493-4c9c323fb1bd
begin
	oxygen_readings = copy(readings);
	for bit_pos in (reading_size - 1):-1:0
	    bit_mask = 1 << bit_pos;
	    mapped_bits = (((bit_mask .& oxygen_readings) .> 0) .<< 1) .- 1;
	    mapped_bit_sum = sum(mapped_bits);
	    common_mapped_bit = (mapped_bit_sum > 0) - (mapped_bit_sum < 0);
	    if common_mapped_bit != 0
	        oxygen_readings = oxygen_readings[mapped_bits .== common_mapped_bit];
	    else
	        oxygen_readings = oxygen_readings[mapped_bits .== 1];
	    end
	    if length(oxygen_readings) == 1
	        break;
	    end;
	end;
	oxygen_readings
end

# ╔═╡ 4c88c437-40e7-499b-89a7-2cd1fb0b801d
begin
	c02_readings = copy(readings);
	for bit_pos in (reading_size - 1):-1:0
	    bit_mask = 1 << bit_pos;
	    mapped_bits = (((bit_mask .& c02_readings) .> 0) .<< 1) .- 1;
	    mapped_bit_sum = sum(mapped_bits);
	    common_mapped_bit = (mapped_bit_sum > 0) - (mapped_bit_sum < 0);
	    least_common_mapped_bit = common_mapped_bit * -1;
	    if least_common_mapped_bit != 0
	        c02_readings = c02_readings[mapped_bits .== least_common_mapped_bit];
	    else
	        c02_readings =  c02_readings[mapped_bits .== -1];
	    end
	    if length(c02_readings) == 1
	        break;
	    end;
	end;
	c02_readings
end

# ╔═╡ e6e127b1-0865-4af3-838f-d644b375f442
(oxygen_readings[1], c02_readings[1], oxygen_readings[1] * c02_readings[1])

# ╔═╡ Cell order:
# ╟─695cdeaa-56a8-11ec-2ea0-67a71259749e
# ╠═1457d0de-e91b-44d1-a116-d74abe387c89
# ╠═9fcf7c54-1c01-482d-9947-7b6f7ac99570
# ╟─290f93c4-27ff-4857-8a47-00f2cb0f65c7
# ╠═3c8b3203-77cd-4699-8493-4c9c323fb1bd
# ╠═4c88c437-40e7-499b-89a7-2cd1fb0b801d
# ╠═e6e127b1-0865-4af3-838f-d644b375f442
