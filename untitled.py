print "Total Unmatched Stories", len(unmatched)
print "Total Matched Stories", len(matched), "OR", "%.2f" % float(len(matched) / (.01* len(unmatched))),'%'

print "Number of Unmatched Stories about Clinton", len(clinton_unmatch), "%.2f" % float(len(clinton_unmatch) / (.01* len(unmatched))),'% of the Unmatched'
print "Number of Unmatched Stories about Trump", len(trump_unmatch), "%.2f" % float(len(trump_unmatch) / (.01* len(unmatched))),'%'
print "Number of Unmatched Stories about Sanders", len(sanders_unmatch),"%.2f" % float(len(sanders_unmatch) / (.01* len(unmatched))),'%'
print "Number of Unmatched Stories about Cruz", len(cruz_unmatch), "%.2f" % float(len(cruz_unmatch) / (.01* len(unmatched))),'%'