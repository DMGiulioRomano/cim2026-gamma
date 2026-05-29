REPO_DIR    := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PAPER_DIR   := $(REPO_DIR)paper
WORKS_DIR   := $(REPO_DIR)works
RAW_DIR     := $(REPO_DIR)raw
GAMMA_DIR   := $(RAW_DIR)/GAMMA

PAPER_TEX   := $(PAPER_DIR)/cim2026.tex
PAPER_PDF   := $(PAPER_DIR)/cim2026.pdf
WORKS_PDF   := $(WORKS_DIR)/application_form_filled.pdf
AUDIO_LINK  := $(WORKS_DIR)/audio_link.txt

SUBMISSION_DIR := $(REPO_DIR)submission

# Identificatori autore da bloccare in PDF anonimizzati.
# Estendere se nuovi alias emergono.
ANON_PATTERNS := De Mattia|Giulio|DMGiulioRomano|giuliodemattia|DeMattia

.PHONY: all paper paper-clean works anonymize-check \
        submission-works submission-paper \
        wiki-lint clean clean-latex help

all: help

help:
	@echo "Targets:"
	@echo "  make paper                - compila $(PAPER_PDF) + anonymize-check"
	@echo "  make works                - verifica completezza works/ + anonymize-check"
	@echo "  make anonymize-check      - greppa metadati PDF per identificatori autore"
	@echo "  make submission-works     - bundle Works per EasyChair upload"
	@echo "  make submission-paper     - bundle Paper anonimizzato per EasyChair upload"
	@echo "  make wiki-lint            - lint pagine wiki (orphan, link rotti)"
	@echo "  make paper-clean          - rm artefatti LaTeX da paper/"
	@echo "  make clean                - paper-clean + rm submission/ + inbox/"

# ---------- Paper ----------

paper: $(PAPER_TEX)
	@if [ ! -f $(PAPER_DIR)/refs.bib ]; then \
		echo "WARN: $(PAPER_DIR)/refs.bib mancante — bibtex fallirà"; \
	fi
	cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode cim2026.tex
	cd $(PAPER_DIR) && bibtex cim2026 || echo "WARN: bibtex fallito (refs.bib mancante o vuoto)"
	cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode cim2026.tex
	cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode cim2026.tex
	@$(MAKE) anonymize-check

paper-clean:
	rm -f $(PAPER_DIR)/cim2026.aux $(PAPER_DIR)/cim2026.log \
	      $(PAPER_DIR)/cim2026.out $(PAPER_DIR)/cim2026.toc \
	      $(PAPER_DIR)/cim2026.bbl $(PAPER_DIR)/cim2026.blg \
	      $(PAPER_DIR)/cim2026.fls $(PAPER_DIR)/cim2026.fdb_latexmk \
	      $(PAPER_DIR)/cim2026.synctex.gz

# ---------- Works ----------

works:
	@echo "Verifica completezza works/..."
	@test -f $(WORKS_PDF) || { echo "ERR: $(WORKS_PDF) mancante"; exit 1; }
	@test -f $(AUDIO_LINK) || { echo "ERR: $(AUDIO_LINK) mancante"; exit 1; }
	@grep -qE '^url:\s*https?://' $(AUDIO_LINK) || { echo "ERR: $(AUDIO_LINK) manca riga 'url:'"; exit 1; }
	@grep -qE '^commit:\s*[0-9a-f]{7,40}' $(AUDIO_LINK) || { echo "ERR: $(AUDIO_LINK) manca riga 'commit:'"; exit 1; }
	@grep -qE '^sha256:\s*[0-9a-f]{64}' $(AUDIO_LINK) || { echo "ERR: $(AUDIO_LINK) manca riga 'sha256:'"; exit 1; }
	@echo "OK: works/ completo (anonimato non richiesto per Works track)"

# ---------- Anonimizzazione ----------

# Esce nonzero se trova identificatori autore in metadati o testo del PDF Paper
# (Paper track e' double-blind; Works track NON richiede anonimato).
# Richiede `pdfinfo` (poppler) e `pdftotext`.
anonymize-check:
	@echo "anonymize-check (solo Paper): pattern = $(ANON_PATTERNS)"
	@command -v pdfinfo >/dev/null || { echo "ERR: pdfinfo non trovato (brew install poppler)"; exit 1; }
	@command -v pdftotext >/dev/null || { echo "ERR: pdftotext non trovato (brew install poppler)"; exit 1; }
	@failed=0; \
	if [ -f $(PAPER_PDF) ]; then \
		echo "  scan: $(PAPER_PDF)"; \
		if pdfinfo $(PAPER_PDF) | grep -iE "$(ANON_PATTERNS)"; then \
			echo "    FAIL: metadati contengono identificatore autore"; failed=1; \
		fi; \
		if pdftotext $(PAPER_PDF) - | grep -iE "$(ANON_PATTERNS)"; then \
			echo "    FAIL: testo PDF contiene identificatore autore"; failed=1; \
		fi; \
	else \
		echo "  $(PAPER_PDF) non esiste, skip"; \
	fi; \
	if [ $$failed -eq 1 ]; then \
		echo "anonymize-check: FAIL"; exit 1; \
	else \
		echo "anonymize-check: OK"; \
	fi

# ---------- Submission bundle ----------

submission-works: works
	mkdir -p $(SUBMISSION_DIR)
	cp $(WORKS_PDF) $(SUBMISSION_DIR)/Gamma_application_form.pdf
	cp $(AUDIO_LINK) $(SUBMISSION_DIR)/Gamma_audio_link.txt
	@echo "Bundle Works pronto in $(SUBMISSION_DIR)/"

submission-paper: paper
	mkdir -p $(SUBMISSION_DIR)
	cp $(PAPER_PDF) $(SUBMISSION_DIR)/Gamma_paper_anonymous.pdf
	@echo "Bundle Paper pronto in $(SUBMISSION_DIR)/"

# ---------- Wiki ----------

# Lint: cerca pagine in wiki/sources e wiki/concepts mai linkate da index.md
wiki-lint:
	@if [ ! -f $(REPO_DIR)wiki/index.md ]; then \
		echo "ERR: wiki/index.md mancante"; exit 1; \
	fi
	@orphans=0; \
	for f in $$(find $(REPO_DIR)wiki/sources $(REPO_DIR)wiki/concepts -name "*.md" 2>/dev/null); do \
		base=$$(basename $$f); \
		if ! grep -q "$$base" $(REPO_DIR)wiki/index.md; then \
			echo "orphan: $$f"; orphans=1; \
		fi; \
	done; \
	if [ $$orphans -eq 1 ]; then \
		echo "wiki-lint: pagine orfane trovate"; exit 1; \
	else \
		echo "wiki-lint: OK"; \
	fi

# ---------- Clean ----------

clean: paper-clean
	rm -rf $(SUBMISSION_DIR)
	rm -rf $(REPO_DIR)inbox/*

clean-latex: paper-clean
