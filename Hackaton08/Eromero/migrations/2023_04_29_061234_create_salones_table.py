from orator.migrations import Migration


class CreateSalonesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('salones') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('capacidad')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('salones')
