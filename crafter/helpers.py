
def cartesian_to_isometric( cartX, cartY ):
	return (cartX - cartY, (cartX - cartY) / 2)

def isometric_to_cartesian( isoX, isoY ):
	return ((2 * isoY + isoX) / 2, (2 * isoY - isoX) / 2)