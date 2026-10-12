srpm:
	-dnf -y install spectool rpmautospec rpkg
	spectool -g $(spec)
	rpmautospec process-distgit $(spec) $(outdir)/$(notdir $(spec))
	rpkg srpm --spec $(outdir)/$(notdir $(spec)) --outdir $(outdir)
