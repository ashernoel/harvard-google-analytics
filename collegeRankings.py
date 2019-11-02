from googleTrendsUpgrade import *

colleges_HYPSM = ["Harvard University", 'Stanford University',
                      'Massachusetts Institute of Technology', 'Princeton University',
                      'Yale University']

colleges_ivyLeague = ["Harvard University", "Brown University", "Columbia University",
                      "Dartmouth College", "University of Pennsylvania", "Princeton University",
                      "Yale University", "Cornell University", "Northeastern University"]

colleges_USNews = ["Princeton University", "Harvard University", "Columbia University",
                   "Massachusetts Institute of Technology", "Yale University", "Stanford University",
                   "University of Chicago", "University of Pennsylvania", "Northwestern University", "Duke University",
                   "Johns Hopkins University","California Institute of Technology", "Dartmouth College",
                   "Brown University", "University of Notre Dame", "Vanderbilt University", "Cornell University",
                   "Rice University", "Washington University in St. Louis", "University of California: Los Angeles",
                   "Emory University", "University of California: Berkeley", "University of Southern California",
                   "Georgetown University", "Carnegie Mellon University", "University of Michigan: Ann Arbor",
                   "Wake Forest University", "University of Virginia",
                   "Georgia Institute of Technology", "New York University"]

bostonMetro = 'US-NH-506'
sanfranMetro = 'US-CA-807'
newYorkMetro = 'US-NY-501'
chicagoMetro = 'US-IN-602'

ivyUS = getTrendsData(colleges_USNews, chicagoMetro, 'today 5-y', True)

# Rename the columns so they in english again in the same order as the original list
ivyUSOut = getAnnualAverages(ivyUS, 5, 2015)

print(ivyUSOut)

plotLine(ivyUSOut.iloc[:, ::-1], "Domestic Ivy League Search Data Over Time")
plotStackedHist(ivyUSOut.iloc[:, ::-1], "Domestic Ivy League Search Data Over Time", True)