# for this program, I had installed camelcase via cmd prompt - pip install camelcase(it did not worked)
# open project>settings>Python interpreter>+ icon on top of packages> search for camelcase and click on install(worked)

import camelcase

c = camelcase.CamelCase()
txt = "using camelcase package to change the line"
print(c.hump(txt))
