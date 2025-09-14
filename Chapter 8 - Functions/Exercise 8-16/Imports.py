"""8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *"""

from print_models import display_message
from print_models import describe_city as dc
import print_models as pm
from print_models import *

dc('Tokyo', 'Japan')
pm.display_message()
pm.favorite_book('Python Crash Course by Eric Matthes')
pm.make_shirt(10, 'Hello World!')
