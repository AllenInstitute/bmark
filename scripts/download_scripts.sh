get_bmark_pilot(){
    # downloads files from NeMO, github and google drive.

    TARGET_DIR="$1/"
    echo "Downloading data to "$TARGET_DIR

    # source folder (NeMO)
    SOURCE="https://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/sncell/10x_v3/mouse/processed/analysis/10X_nuclei_v3_AIBS/"

    mkdir $TARGET_DIR
    curl -o $TARGET_DIR"QC.csv" $SOURCE"QC.csv"
    curl -o $TARGET_DIR"barcode.tsv" $SOURCE"barcode.tsv"
    curl -o $TARGET_DIR"sample_metadata.csv" $SOURCE"sample_metadata.csv"
    curl -o $TARGET_DIR"features.tsv.gz" $SOURCE"features.tsv.gz"
    curl -o $TARGET_DIR"matrix.mtx.gz" $SOURCE"matrix.mtx.gz"
    gzip -d $TARGET_DIR"features.tsv.gz"
    gzip -d $TARGET_DIR"matrix.mtx.gz"

    # source folder (Taxonomy)
    SOURCE="https://raw.githubusercontent.com/AllenInstitute/MOp_taxonomies_ontology/main"

    curl -o $TARGET_DIR"nomenclature_table_CCN202002013.csv" $SOURCE"/mouseM1_CCN202002013/nomenclature_table_CCN202002013.csv"
    curl -o $TARGET_DIR"MouseNSForestMarkers_symbols.csv" $SOURCE"/NSForestMarkers/MouseNSForestMarkers_symbols.csv"

    # source is google drive - gdown is a python-based cli utility that must be available
    gdown --id "1ztNHxz5jpS0hqlW-s8iZTNIm0_4gUbhi" -O $TARGET_DIR"metadata.csv"
}