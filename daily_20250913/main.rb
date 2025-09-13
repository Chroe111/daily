require "csv"

summary = Hash.new(0)

CSV.foreach("sales.csv", headers: true) do |row|
  summary[row["product"]] += row["price"].to_i
end

summary.each do |item, sales|
  puts "%s: %d" % [item, sales]
end
