#!/usr/bin/env ruby
puts File.open(ARGV[0]).map { |line| line.scan(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/).map { |match| match.join(",") } }.join("\n")
