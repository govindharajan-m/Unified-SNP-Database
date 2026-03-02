# Unified Genomic Variant Database (UGVD)

## Project Overview
This project presents a normalized relational database designed to integrate and structure scattered biological, clinical, and population genetics data. Currently, critical genomic information is siloed across multiple public repositories. This Database solves this by integrating:

- **dbSNP**: Variant identity and location
- **Ensembl**: Gene mapping and descriptions
- **ClinVar**: Clinical significance and disease associations
- **gnomAD**: Population-specific allele frequencies

By unifying these sources, researchers and clinicians can write rapid, complex SQL queries to correlate pathogenic variants with specific populations or gene functions without writing custom parsing scripts for terabytes of VCF files.
