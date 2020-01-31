require_relative "./kyu-8/even-or-odd/even_or_odd"
require "test/unit"
 
class TestSimpleNumber < Test::Unit::TestCase
 
  def test_even_odd
    assert_equal("Even", even_or_odd(2))
    assert_equal("Even", even_or_odd(0))
    assert_equal("Odd", even_or_odd(7))
    assert_equal("Odd", even_or_odd(1))
    assert_equal("Odd", even_or_odd(-1))
  end
 
end
