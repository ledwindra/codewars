require "test/unit"
require_relative "./kyu-8/even-or-odd/even_or_odd"
require_relative "./kyu-8/sum-positive-number/sum_positive_number"
 
class TestEvenOdd < Test::Unit::TestCase
 
  def test_even_odd
    assert_equal(even_or_odd(2), "Even")
    assert_equal(even_or_odd(0), "Even")
    assert_equal(even_or_odd(7), "Odd")
    assert_equal(even_or_odd(1), "Odd")
    assert_equal(even_or_odd(-1), "Odd")
  end 
end

class TestSumPositive < Test::Unit::TestCase
 
  def test_sum_positive
    assert_equal(positive_sum([1, 2, 3, 4, 5]), 15)
    assert_equal(positive_sum([1,-2,3,4,5]), 13)
    assert_equal(positive_sum([-1,2,3,4,-5]), 9)
  end
end
