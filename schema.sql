-- Gene Table
CREATE TABLE Gene (
    gene_id TEXT PRIMARY KEY,
    gene_name TEXT,
    gene_description TEXT
);

-- SNP Table
CREATE TABLE SNP (
    rsid TEXT PRIMARY KEY,
    gene_id TEXT,
    chromosome TEXT,
    position INTEGER,
    reference_allele TEXT,
    alternate_allele TEXT,
    FOREIGN KEY (gene_id) REFERENCES Gene(gene_id)
);

-- Clinical_Annotation Table
CREATE TABLE Clinical_Annotation (
    clinical_id TEXT PRIMARY KEY,
    rsid TEXT,
    clinical_significance TEXT,
    associated_disease TEXT,
    FOREIGN KEY (rsid) REFERENCES SNP(rsid)
);

-- Population_Frequency Table
CREATE TABLE Population_Frequency (
    rsid TEXT,
    population TEXT,
    allele_frequency REAL,
    PRIMARY KEY (rsid, population),
    FOREIGN KEY (rsid) REFERENCES SNP(rsid)
);
