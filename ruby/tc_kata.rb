require_relative "./kyu-8/even-or-odd/even_or_odd"
require_relative "./kyu-8/another-ruby/another_ruby"
require "test/unit"
 
class TestSimpleNumber < Test::Unit::TestCase
 
  def test_even_odd
    assert_equal("Even", even_or_odd(2))
    assert_equal("Even", even_or_odd(0))
    assert_equal("Odd", even_or_odd(7))
    assert_equal("Odd", even_or_odd(1))
    assert_equal("Odd", even_or_odd(-1))
  end

  def test_another_ruby
    assert_equal("Even", another_ruby(2))
    assert_equal("Even", another_ruby(0))
    assert_equal("Odd", another_ruby(7))
    assert_equal("Odd", another_ruby(1))
    assert_equal("Odd", another_ruby(-1))
  end
 
end
