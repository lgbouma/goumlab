import xml.etree.ElementTree as ET, urllib, gzip, io
url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.urlopen(url).read())))

import matplotlib.pyplot as plt
import numpy as np

# Get number of planets in catalog
N = 0
for planet in oec.findall(".//planet"):
    N += 1

master = np.zeros([N, 3], float)
discovType = np.zeros(N, str)
i = 0
for planet in oec.findall(".//planet"):
    if type(planet.findtext("mass")) is str and len(planet.findtext("mass")) > 0:
        master[i, 0] = float(planet.findtext("mass"))
    if type(planet.findtext("radius")) is str and len(planet.findtext("radius")) > 0:
        master[i, 1] = float(planet.findtext("radius"))
    if type(planet.findtext("semimajoraxis")) is str and len(planet.findtext("semimajoraxis")) > 0:
        master[i, 2] = float(planet.findtext("semimajoraxis"))
    discovType[i] = planet.findtext("discoverymethod")
    i += 1

plotDat = np.zeros([N, 2], float)
plotDat[:, 0] = master[:, 2]
plotDat[:, 1] = master[:, 0]

#Get list of indices of planets with no semimaj or mass data, and delete them from what will be plotted
maIndex = []
for j in range(np.shape(plotDat)[0]):
    if plotDat[j, 0] < 1e-9 or plotDat[j, 1] < 1e-9:
        maIndex.append(j)

maPlotDat = np.delete(plotDat, maIndex, axis=0)
maDiscovType = np.delete(discovType, maIndex, axis=0)

#Get list of indices for R (radial), t (transit), m (microlensing), i (direct imaging)
ri, ti, mi, ii, ni = [], [], [], [], []
for k in range(len(maDiscovType)):
    if maDiscovType[k] == 'R':
        ri.append(k)
    elif maDiscovType[k] == 't':
        ti.append(k)
    elif maDiscovType[k] == 'm':
        mi.append(k)
    elif maDiscovType[k] == 'i':
        ii.append(k)
    elif maDiscovType[k] == 'N':
        ni.append(k)
    else:
        print(k, maDiscovType[k])

radial = maPlotDat[ri]
transit = maPlotDat[ti]
micro = maPlotDat[mi]
dirImag = maPlotDat[ii]
other = maPlotDat[ni]

fig = plt.figure(1)

plt.subplot(2, 2, 1)
ax = plt.gca()
ax.plot(radial[:, 0], radial[:, 1], 'o', c='w', alpha=1.0, markeredgecolor='k', label='Radial velocity')
plt.legend(loc='lower left', numpoints=1)
#plt.text(0.41, 1.3e-6, 'Data from the Open Exoplanet Catalogue. 2015-08-13.', fontsize=12)
plt.xlabel('Semi-major axis [AU]')
plt.ylabel('Mass $[M_J]$')
ax.set_yscale('log')
plt.ylim([1e-6, 1e3])
plt.xlim([1e-2, 1e3])
ax.set_xscale('log')

plt.subplot(2, 2, 2)
ax = plt.gca()
ax.plot(transit[:, 0], transit[:, 1], '*', c='k', alpha=1.0, markeredgecolor='k', label='Transit')
plt.legend(loc='lower left', numpoints=1)
#plt.text(0.41, 1.3e-6, 'Data from the Open Exoplanet Catalogue. 2015-08-13.', fontsize=12)
plt.xlabel('Semi-major axis [AU]')
plt.ylabel('Mass $[M_J]$')
ax.set_yscale('log')
plt.ylim([1e-6, 1e3])
plt.xlim([1e-2, 1e3])
ax.set_xscale('log')

plt.subplot(2, 2, 3)
ax = plt.gca()
ax.plot(micro[:, 0], micro[:, 1], 's', c='orange', alpha=1.0, markeredgecolor='k', label='Microlensing')
plt.legend(loc='lower left', numpoints=1)
#plt.text(0.41, 1.3e-6, 'Data from the Open Exoplanet Catalogue. 2015-08-13.', fontsize=12)
plt.xlabel('Semi-major axis [AU]')
plt.ylabel('Mass $[M_J]$')
ax.set_yscale('log')
plt.ylim([1e-6, 1e3])
plt.xlim([1e-2, 1e3])
ax.set_xscale('log')

plt.subplot(2, 2, 4)
ax = plt.gca()
ax.plot(dirImag[:, 0], dirImag[:, 1], 'v', c='b', alpha=1.0, markeredgecolor='k', label='Direct imaging')
plt.legend(loc='lower left', numpoints=1)
#plt.text(0.41, 1.3e-6, 'Data from the Open Exoplanet Catalogue. 2015-08-13.', fontsize=12)
plt.xlabel('Semi-major axis [AU]')
plt.ylabel('Mass $[M_J]$')
ax.set_yscale('log')
plt.ylim([1e-6, 1e3])
plt.xlim([1e-2, 1e3])
ax.set_xscale('log')

#plt.title('Exoplanet mass v. semi-major axis, segmented')
plt.tight_layout()
plt.show(block=True)


'''
#No discovery type, straight log-log plot
fig = plt.figure(1)     #returns fig instance, numbered 1. gcf() works too
plt.subplot(1, 1, 1)    #(numrows, numcols, fignum). default: plt.subplot(111)
ax = plt.gca()          #returns current axes (matplotlib.axes.Axes instance)
ax.plot(maPlotDat[:, 0], maPlotDat[:, 1], 'o',
        c='red', alpha=1.0, markeredgecolor='black')

plt.text(1.2, 4e-6, 'Data from the Open Exoplanet Catalogue. '
                       '2015-08-13.', fontsize=10)
plt.xlabel('Semi-major axis $[\mathrm{AU}]$', fontsize=16)
plt.ylabel('Mass $[\mathrm{M}_{\mathrm{Jup}}]$', fontsize=16)
ax.set_yscale('log')
plt.ylim([3.01e-6, 1e3])
ax.set_xscale('log')
plt.title('Exoplanet catalogue', fontsize=20)
plt.show()
'''



'''
# Find all circumbinary planets
for planet in oec.findall(".//binary/planet"):
    print planet.findtext("name")

# Output distance to planetary system (in pc, if known) and number of planets in system
for system in oec.findall(".//system"):
    print system.findtext("distance"), len(system.findall(".//planet"))
    '''
