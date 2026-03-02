PRAGMA foreign_keys = ON;

-- 1. Ensembl -> Genes
INSERT INTO Gene (gene_id, gene_name, gene_description) VALUES 
('ENSG00000139618', 'BRCA2', 'BRCA2 DNA repair associated'),
('ENSG00000141510', 'TP53', 'Tumor protein p53');

-- 2. dbSNP -> SNPs
INSERT INTO SNP (rsid, gene_id, chromosome, position, reference_allele, alternate_allele) VALUES 
('rs80359278', 'ENSG00000139618', 'chr13', 32340300, 'A', 'G'),
('rs1042522', 'ENSG00000141510', 'chr17', 7675088, 'C', 'G');

-- 3. ClinVar -> Clinical Annotations
INSERT INTO Clinical_Annotation (clinical_id, rsid, clinical_significance, associated_disease) VALUES 
('RCV000042456', 'rs80359278', 'Pathogenic', 'Hereditary breast and ovarian cancer syndrome'),
('RCV000015525', 'rs1042522', 'Benign', 'Li-Fraumeni syndrome');

-- 4. gnomAD -> Population Frequencies
INSERT INTO Population_Frequency (rsid, population, allele_frequency) VALUES 
('rs80359278', 'European (Non-Finnish)', 0.00001),
('rs80359278', 'African/African American', 0.00005),
('rs1042522', 'Global', 0.45);
