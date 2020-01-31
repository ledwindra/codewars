def positive_sum(arr)
  if arr.empty? or arr.all?(&:negative?) then
    return 0
  else
    for i in 0..(arr.length - 1) do
      if arr[i] < 0 then
        arr[i] = 0
      end
    end
  end
  
  return arr.sum

end