/*
A KBase module: kb_hisat2
*/

module kb_hisat2 {
/* indicates true or false values, false <= 0, true >=1 */
    typedef int bool;

/*
    Input for hisat2.
    ws_name = the workspace name provided by the narrative for storing output.
    sampleset_ref = the workspace reference for either the reads library or set of reads libraries to align.
                  accepted types: KBaseSets.ReadsSet, KBaseRNASeq.RNASeqSampleSet,
                                  KBaseAssembly.SingleEndLibrary, KBaseAssembly.PairedEndLibrary,
                                  KBaseFile.SingleEndLibrary, KBaseFile.PairedEndLibrary
    genome_ref = the workspace reference for the reference genome that HISAT2 will align against.
    num_threads = the number of threads to tell hisat to use (default 2)
    quality_score = one of phred33 or phred64
    skip = number of initial reads to skip (default 0)
    trim3 = number of bases to trim off of the 3' end of each read (default 0)
    trim5 = number of bases to trim off of the 5' end of each read (default 0)
    np = penalty for positions wither the read and/or the reference are an ambiguous character (default 1)
    minins = minimum fragment length for valid paired-end alignments. only used if no_spliced_alignment is true
    maxins = maximum fragment length for valid paired-end alignments. only used if no_spliced_alignment is true
    orientation = orientation of each member of paired-end reads. valid values = "fr, rf, ff"
    min_intron_length = sets minimum intron length (default 20)
    max_intron_length = sets maximum intron length (default 500,000)
    no_spliced_alignment = disable spliced alignment
    transcriptome_mapping_only = only report alignments with known transcripts
    tailor_alignments = report alignments tailored for either cufflinks or stringtie
    condition = a string stating the experimental condition of the reads. REQUIRED for single reads,
                ignored for sets.
    build_report = 1 if we build a report, 0 otherwise. (default 1) (shouldn't be user set - mainly used for subtasks)
    output naming:
        alignment_suffix is appended to the name of each individual reads object name (just the one if
        it's a simple input of a single reads library, but to each if it's a set)
        alignmentset_suffix is appended to the name of the reads set, if a set is passed.
*/
    typedef structure {
        string ws_name;
        string alignment_suffix;
        string alignmentset_suffix;
        string sampleset_ref;
        string condition;
        string genome_ref;
        int num_threads;
        string quality_score;
        int skip;
        int trim3;
        int trim5;
        int np;
        int minins;
        int maxins;
        string orientation;
        int min_intron_length;
        int max_intron_length;
        bool no_spliced_alignment;
        bool transcriptome_mapping_only;
        string tailor_alignments;
        bool build_report;
    } Hisat2Params;


/*
    Created alignment object returned.
    alignment_ref = the workspace reference of the new alignment object
    name = the name of the new object, for convenience.
*/
    typedef structure {
        string alignment_ref;
        string name;
    } AlignmentObj;

/*
    Output for hisat2.
    alignmentset_ref if an alignment set is created
    alignment_objs for each individual alignment created. The keys are the references to the reads
        object being aligned.
*/
    typedef structure {
		string report_name;
		string report_ref;
        string alignmentset_ref;
        mapping<string reads_ref, AlignmentObj> alignment_objs;
    } Hisat2Output;

    funcdef run_hisat2(Hisat2Params params)
        returns(Hisat2Output) authentication required;
};
