get_bmark_pilot(){
    TARGET_DIR="$1/"
    echo "Downloading data to "$TARGET_DIR

    # source folder (remote)
    SOURCE="https://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/sncell/10x_v3/mouse/processed/analysis/10X_nuclei_v3_AIBS/"

    mkdir $TARGET_DIR
    curl -o $TARGET_DIR"QC.csv" $SOURCE"QC.csv"
    curl -o $TARGET_DIR"barcode.tsv" $SOURCE"barcode.tsv"
    curl -o $TARGET_DIR"sample_metadata.csv" $SOURCE"sample_metadata.csv"
    curl -o $TARGET_DIR"features.tsv.gz" $SOURCE"features.tsv.gz"
    curl -o $TARGET_DIR"matrix.mtx.gz" $SOURCE"matrix.mtx.gz"
    gdown --id "1ztNHxz5jpS0hqlW-s8iZTNIm0_4gUbhi" -O $SOURCE"metadata.csv"

    gzip -d $TARGET_DIR"features.tsv.gz"
    gzip -d $TARGET_DIR"matrix.mtx.gz"
}

