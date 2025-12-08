CC = gcc

# opções de compilação (sem -lm aqui)
CFLAGS = -fopenmp

# bibliotecas para link (colocadas ao final)
LDLIBS = -lm

SEQ_DIR = src/seq
OMP_DIR = src/omp
BUILD_SEQ = build/seq
BUILD_OMP = build/omp

SEQ_SRCS = $(wildcard $(SEQ_DIR)/*.c)
OMP_SRCS = $(wildcard $(OMP_DIR)/*.c)

SEQ_BINS = $(patsubst $(SEQ_DIR)/%.c, $(BUILD_SEQ)/%, $(SEQ_SRCS))
OMP_BINS = $(patsubst $(OMP_DIR)/%.c, $(BUILD_OMP)/%, $(OMP_SRCS))

all: $(SEQ_BINS) $(OMP_BINS)

$(BUILD_SEQ)/%: $(SEQ_DIR)/%.c
	@mkdir -p $(BUILD_SEQ)
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

$(BUILD_OMP)/%: $(OMP_DIR)/%.c
	@mkdir -p $(BUILD_OMP)
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

clean:
	rm -rf build

.PHONY: all clean
