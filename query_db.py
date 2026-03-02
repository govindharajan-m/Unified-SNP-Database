import sqlite3
import os

def check_genomics_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'genomics.db')
    
    if not os.path.exists(db_path):
        print("Database not found. Please run etl_pipeline.py first.")
        return
        
    print(f"Connecting to {db_path}...\n")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Show all genes
    cursor.execute("SELECT * FROM Gene")
    genes = cursor.fetchall()
    print("--- GENES ---")
    for row in genes:
        print(row)
        
    # 2. Show all SNPs and their linked genes
    cursor.execute("""
        SELECT SNP.rsid, SNP.chromosome, SNP.position, Gene.gene_name 
        FROM SNP 
        JOIN Gene ON SNP.gene_id = Gene.gene_id
    """)
    snps = cursor.fetchall()
    print("\n--- SNPs ---")
    for row in snps:
        print(row)
        
    # 3. Show Clinical Annotations
    cursor.execute("""
        SELECT SNP.rsid, Clinical_Annotation.clinical_significance, Clinical_Annotation.associated_disease 
        FROM Clinical_Annotation
        JOIN SNP ON Clinical_Annotation.rsid = SNP.rsid
    """)
    clinical = cursor.fetchall()
    print("\n--- CLINICAL ANNOTATIONS ---")
    for row in clinical:
        print(row)
        
    # 4. Show Population Frequencies
    cursor.execute("""
        SELECT SNP.rsid, Population_Frequency.population, Population_Frequency.allele_frequency
        FROM Population_Frequency
        JOIN SNP ON Population_Frequency.rsid = SNP.rsid
    """)
    freqs = cursor.fetchall()
    print("\n--- POPULATION FREQUENCIES ---")
    for row in freqs:
        print(row)

    conn.close()

if __name__ == "__main__":
    check_genomics_db()
