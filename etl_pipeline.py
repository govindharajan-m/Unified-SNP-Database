import sqlite3
import os

def setup_database():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'genomics.db')
    schema_path = os.path.join(base_dir, 'schema.sql')
    
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing database at {db_path}")

    print(f"Connecting to database at {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    
    print("Executing schema...")
    with open(schema_path, 'r') as file:
        schema_script = file.read()
    cursor.executescript(schema_script)
    
    # 1. Ensembl -> Genes
    print("Loading Ensembl Data (Genes)...")
    genes = [
        ('ENSG00000139618', 'BRCA2', 'BRCA2 DNA repair associated'),
        ('ENSG00000141510', 'TP53', 'Tumor protein p53')
    ]
    cursor.executemany("INSERT INTO Gene (gene_id, gene_name, gene_description) VALUES (?, ?, ?)", genes)

    # 2. dbSNP -> SNPs
    print("Loading dbSNP Data (Variants)...")
    snps = [
        ('rs80359278', 'ENSG00000139618', 'chr13', 32340300, 'A', 'G'),
        ('rs1042522', 'ENSG00000141510', 'chr17', 7675088, 'C', 'G')
    ]
    cursor.executemany("INSERT INTO SNP (rsid, gene_id, chromosome, position, reference_allele, alternate_allele) VALUES (?, ?, ?, ?, ?, ?)", snps)

    # 3. ClinVar -> Clinical Annotations
    print("Loading ClinVar Data (Clinical Annotations)...")
    clinvar_data = [
        ('RCV000042456', 'rs80359278', 'Pathogenic', 'Hereditary breast and ovarian cancer syndrome'),
        ('RCV000015525', 'rs1042522', 'Benign', 'Li-Fraumeni syndrome')
    ]
    cursor.executemany("INSERT INTO Clinical_Annotation (clinical_id, rsid, clinical_significance, associated_disease) VALUES (?, ?, ?, ?)", clinvar_data)

    # 4. gnomAD -> Population Frequencies
    print("Loading gnomAD Data (Population Frequencies)...")
    gnomad_data = [
        ('rs80359278', 'European (Non-Finnish)', 0.00001),
        ('rs80359278', 'African/African American', 0.00005),
        ('rs1042522', 'Global', 0.45) # Common variant
    ]
    cursor.executemany("INSERT INTO Population_Frequency (rsid, population, allele_frequency) VALUES (?, ?, ?)", gnomad_data)

    conn.commit()
    print("Database successfully populated with sample ETL data!")
    conn.close()

if __name__ == "__main__":
    setup_database()
