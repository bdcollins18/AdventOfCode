### A Pluto.jl notebook ###
# v0.17.2

using Markdown
using InteractiveUtils

# ╔═╡ dbfaa2ea-56a7-11ec-0fbe-cd9ce336f202
html"<article class=\"day-desc\"><h2>--- Day 2: Dive! ---</h2><p>Now, you need to figure out how to <span title=\"Tank, I need a pilot program for a B212 helicopter.\">pilot this thing</span>.</p>
<p>It seems like the submarine can take a series of commands like <code>forward 1</code>, <code>down 2</code>, or <code>up 3</code>:</p>
<ul>
<li><code>forward X</code> increases the horizontal position by <code>X</code> units.</li>
<li><code>down X</code> <em>increases</em> the depth by <code>X</code> units.</li>
<li><code>up X</code> <em>decreases</em> the depth by <code>X</code> units.</li>
</ul>
<p>Note that since you're on a submarine, <code>down</code> and <code>up</code> affect your <em>depth</em>, and so they have the opposite result of what you might expect.</p>
<p>The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:</p>
<pre><code>forward 5
down 5
forward 8
up 3
down 8
forward 2
</code></pre>
<p>Your horizontal position and depth both start at <code>0</code>. The steps above would then modify them as follows:</p>
<ul>
<li><code>forward 5</code> adds <code>5</code> to your horizontal position, a total of <code>5</code>.</li>
<li><code>down 5</code> adds <code>5</code> to your depth, resulting in a value of <code>5</code>.</li>
<li><code>forward 8</code> adds <code>8</code> to your horizontal position, a total of <code>13</code>.</li>
<li><code>up 3</code> decreases your depth by <code>3</code>, resulting in a value of <code>2</code>.</li>
<li><code>down 8</code> adds <code>8</code> to your depth, resulting in a value of <code>10</code>.</li>
<li><code>forward 2</code> adds <code>2</code> to your horizontal position, a total of <code>15</code>.</li>
</ul>
<p>After following these instructions, you would have a horizontal position of <code>15</code> and a depth of <code>10</code>. (Multiplying these together produces <code><em>150</em></code>.)</p>
<p>Calculate the horizontal position and depth you would have after following the planned course. <em>What do you get if you multiply your final horizontal position by your final depth?</em></p>
</article>"

# ╔═╡ fee29897-937d-4439-a653-eff9486e794a
function to_command_tuple(sub_command)
    fields = split(sub_command, " ");
    return (fields[1], parse(Int64, fields[2]));
end;

# ╔═╡ 3fb31af9-3dd9-4628-8856-466512ed0c16
input = [to_command_tuple(sub_command) for sub_command in readlines("input.txt")];

# ╔═╡ 829c6cdd-b46a-4f81-ba21-5829f39e4122
begin
	local horizontal = 0;
	local depth = 0;
	for command in input
	    if command[1] == "up"
	        depth -= command[2];
	    elseif command[1] == "down"
	        depth += command[2];
	    elseif command[1] == "forward"
	        horizontal += command[2];
	    end
	end;
	(horizontal, depth, horizontal * depth)
end

# ╔═╡ 9d50365c-0e82-40d7-b908-63ed28bca9a6
html"<article class=\"day-desc\"><h2 id=\"part2\">--- Part Two ---</h2><p>Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.</p>
<p>In addition to horizontal position and depth, you'll also need to track a third value, <em>aim</em>, which also starts at <code>0</code>. The commands also mean something entirely different than you first thought:</p>
<ul>
<li><code>down X</code> <em>increases</em> your aim by <code>X</code> units.</li>
<li><code>up X</code> <em>decreases</em> your aim by <code>X</code> units.</li>
<li><code>forward X</code> does two things:<ul>
  <li>It increases your horizontal position by <code>X</code> units.</li>
  <li>It increases your depth by your aim <em>multiplied by</em> <code>X</code>.</li>
</ul></li>
</ul>
<p>Again note that since you're on a submarine, <code>down</code> and <code>up</code> do the opposite of what you might expect: \"down\" means aiming in the positive direction.</p>
<p>Now, the above example does something different:</p>
<ul>
<li><code>forward 5</code> adds <code>5</code> to your horizontal position, a total of <code>5</code>. Because your aim is <code>0</code>, your depth does not change.</li>
<li><code>down 5</code> adds <code>5</code> to your aim, resulting in a value of <code>5</code>.</li>
<li><code>forward 8</code> adds <code>8</code> to your horizontal position, a total of <code>13</code>. Because your aim is <code>5</code>, your depth increases by <code>8*5=40</code>.</li>
<li><code>up 3</code> decreases your aim by <code>3</code>, resulting in a value of <code>2</code>.</li>
<li><code>down 8</code> adds <code>8</code> to your aim, resulting in a value of <code>10</code>.</li>
<li><code>forward 2</code> adds <code>2</code> to your horizontal position, a total of <code>15</code>.  Because your aim is <code>10</code>, your depth increases by <code>2*10=20</code> to a total of <code>60</code>.</li>
</ul>
<p>After following these new instructions, you would have a horizontal position of <code>15</code> and a depth of <code>60</code>. (Multiplying these produces <code><em>900</em></code>.)</p>
<p>Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. <em>What do you get if you multiply your final horizontal position by your final depth?</em></p>
</article>"

# ╔═╡ 63dcc867-2eec-40fd-856a-f192bc66d2ec
begin
	local horizontal = 0;
	local depth = 0;
	local aim = 0
	for command in input
	    if command[1] == "up"
	        aim -= command[2];
	    elseif command[1] == "down"
	        aim += command[2];
	    elseif command[1] == "forward"
	        horizontal += command[2];
	        depth += aim * command[2]
	    end
	end;
	(horizontal, depth, horizontal * depth)
end

# ╔═╡ Cell order:
# ╟─dbfaa2ea-56a7-11ec-0fbe-cd9ce336f202
# ╠═fee29897-937d-4439-a653-eff9486e794a
# ╠═3fb31af9-3dd9-4628-8856-466512ed0c16
# ╠═829c6cdd-b46a-4f81-ba21-5829f39e4122
# ╟─9d50365c-0e82-40d7-b908-63ed28bca9a6
# ╠═63dcc867-2eec-40fd-856a-f192bc66d2ec
